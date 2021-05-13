n,c,k=map(int,input().split())
T=[int(input()) for i in range(n)]
T.sort()
ans=1
now=T[0]
pas=0 #passenger

for t in T:
    pas+=1
    if t>now+k or pas>c:
        ans+=1
        now=t
        pas=1

print(ans)