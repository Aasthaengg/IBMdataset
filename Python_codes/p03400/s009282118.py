N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X

for a in A:
    eat_date = [1 + a * i for i in range(100) if 1 + a * i <= D]
    ans += len(eat_date)

print(ans)