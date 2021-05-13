n,m,c = map(int, input().split())
b = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for a in A:
    if sum([x*y for (x,y) in zip(a,b)])+c > 0: ans += 1
print(ans)