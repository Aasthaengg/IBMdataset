n=int(input())
s=input()
t=sorted(s)
t.append("X")
cnt=1
ans=1
for i in range(n):
    if t[i]==t[i+1]:
        cnt+=1
    else:
        ans*=(cnt+1)
        cnt=1
print((ans-1)%(10**9+7))