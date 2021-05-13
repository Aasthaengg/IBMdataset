def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]



n = I()
ans = 0
for i in range(1,n+1):
    for j in range(i,n+1,i):
        ans += j
print(ans)