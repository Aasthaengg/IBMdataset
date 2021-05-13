N=int(input())
d=list(map(int, input().split()))
 
d=sorted(d)
ans=0
 
for i in range(1+10**5):
    if d[int(N/2-1)] < i and i <= d[int(N/2)]:
        ans +=1
 
print(ans)