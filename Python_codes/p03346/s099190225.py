N = int(input())
P = [int(input()) for _ in [0]*N]
m = [0]*N
for i,p in enumerate(P): m[p-1] = i
ans = 0
c = 0
j=-1
for i in m:
    c = (c+1) if j<i else 1
    j=i
    ans = max(ans,c)
print(N-ans)