s=input()
k=int(input())
s1=[]
num1=1
str1=s[0]
for i in range(1,len(s)):
    if str1==s[i]:
        num1+=1
    else:
        s1.append([str1,num1])
        num1=1
        str1=s[i]
s1.append([str1,num1])
if len(s1)>1:
    if s1[0][0]!=s1[-1][0]:
        num2=0
        for i in range(len(s1)):
            num2+=s1[i][1]//2
        print(k*num2)
    else:
        num2=0
        num3=s1[0][1]//2
        num4=s1[-1][1]//2
        num5=(s1[0][1]+s1[-1][1])//2
        for i in range(1,len(s1)-1):
            num2+=s1[i][1]//2
        print((num2*k)+(num5*(k-1))+num3+num4)
else:
    print((len(s)*k)//2)
