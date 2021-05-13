n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for b in a:
    ans += b[1]-b[0]+1
print(ans)
