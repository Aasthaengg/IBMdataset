n = int(input())
d, x = map(int, input().split())
A = [int(input()) for _ in range(n)]

ans = x
for a in A: ans += (d - 1) // a + 1
print(ans)