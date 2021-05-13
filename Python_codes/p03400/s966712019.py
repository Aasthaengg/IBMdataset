N = int(input())
D, X = map(int, input().split())
print(sum((D - 1) // int(input()) + 1 for _ in range(N)) + X)