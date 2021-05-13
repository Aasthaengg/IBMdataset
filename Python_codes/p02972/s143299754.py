n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
for i in range(n):
    num1=n-i
    num2=0
    for j in range((n//num1)-1):
        num2+=ans[num1*(j+2)-1]
    num2%=2
    ans[-1-i]=(num2+a[-1-i])%2
print(ans.count(1))
ans2=[]
for i in range(n):
    if ans[i]==1:
        ans2.append(i+1)
if len(ans2)!=0:
    print(*ans2)
