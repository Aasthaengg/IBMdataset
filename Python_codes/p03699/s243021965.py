n=int(input())
s=[int(input())for _ in range(n)]
ans=sum(s)

x=[]
for i in range(n):
    if s[i]%10 != 0:
        x.append(s[i])
if ans%10 != 0:
    print(ans)
elif len(x)>=1:
    print(ans-min(x))
else:
    print(0)