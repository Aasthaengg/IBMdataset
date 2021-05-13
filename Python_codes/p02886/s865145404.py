from itertools import combinations
n=int(input())
d=list(map(int,input().split()))
c = list(combinations(d,2))
ans = 0
for i,j in c:
    ans += (i*j)
print(ans)