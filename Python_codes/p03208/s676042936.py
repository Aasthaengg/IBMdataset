def inp():return map(int,input().split())
def ip():return int(input())

n,k=inp()
h=[]
for _ in range(n):
    h.append(ip())
h.sort()

ans=10**18
i=0
while i+k-1<n:
    ans=min(ans,h[i+k-1]-h[i])
    i+=1
print(ans)