N = int(input())
D,X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X + sum([-(-D//a) for a in A])

print(ans)