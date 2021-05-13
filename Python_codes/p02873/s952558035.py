s=list(input())
num=[]
str1="<"
if s[0]=="<":
    num1=1
else:
    num.append(0)
    str1=">"
    num1=1
for i in range(len(s)-1):
    if str1==s[i+1]:
        num1+=1
    else:
        if str1=="<":
            str1=">"
        else:
            str1="<"
        num.append(num1)
        num1=1
num.append(num1)
ans=0
if str1=="<":
    num.append(0)
for i in range(len(num)//2):
    ans+=((num[i*2]+1)*num[i*2])//2
    ans+=((num[i*2+1]+1)*num[i*2+1])//2
    ans-=min(num[i*2],num[i*2+1])
print(ans)
