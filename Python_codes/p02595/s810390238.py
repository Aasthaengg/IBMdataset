n,D  = map(int,input().split())
D = D**2
ans = 0

for i in range(n):
    x,y = map(int,input().split())
    if x **2 + y**2 <= D:
        ans += 1

print(ans)
