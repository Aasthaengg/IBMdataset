N, X = map(int, input().split())
m = sorted([int(input()) for _ in range(N)])
rem = X - sum(m)
print(rem// m[0] + N)