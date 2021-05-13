N=int(input())
h=[int(x) for x in input().split()]

ans=h[0]

for i in range(1,N):
    if h[i-1]<h[i]:
        ans+=h[i]-h[i-1]

print(ans)