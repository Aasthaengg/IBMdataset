s=list(input())
num=[]
num1=1
str1="R"
for i in range(1,len(s)):
    if s[i]==str1:
        num1+=1
    else:
        num.append(num1)
        num1=1
        if str1=="R":
            str1="L"
        else:
            str1="R"
num.append(num1)
num2=-1
ans=[0]*len(s)
for i in range(len(num)//2):
    num3=num2+num[i*2]
    ans[num3]=-(num[i*2]//-2)+(num[i*2+1]//2)
    ans[num3+1]=(num[i*2]//2)-(num[i*2+1]//-2)
    num2+=num[i*2]+num[i*2+1]
print(*ans)
