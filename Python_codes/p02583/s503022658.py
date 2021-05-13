from itertools import combinations
n = int(input())
L = list(map(int,input().split()))
ans = 0
for x in combinations(L,3):
    a,b,c = map(int,x)
    if a == b or b == c or c == a:
        continue
    ans += (2*max(a,b,c) < a+b+c)
print(ans)