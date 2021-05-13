n=int(input())

ans = 0

for _ in range(n):
    a, b = (int(x) for x in input().split())
    ans += b-a+1
print(ans)