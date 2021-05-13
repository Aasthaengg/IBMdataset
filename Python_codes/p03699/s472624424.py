n=int(input())
s=[int(input()) for _ in range(n)]
num=sum(s)
ans=0
if num%10!=0:
    ans=num
else:
    for i in range(n):
        num2=num-s[i]
        if num2%10!=0 and ans<num2:
            ans=num2
print(ans)
