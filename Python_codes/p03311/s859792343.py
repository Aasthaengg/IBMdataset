n=int(input())
al=list(map(int,input().split()))
t=[]
for i in range(n):
    t.append(al[i]-(i+1))
t=sorted(t)
if n%2==0:
    v=(t[n//2-1]+t[n//2])//2
else:
    v=t[n//2]
ans=0
for i in t:
    ans+=abs(i-v)
print(ans)