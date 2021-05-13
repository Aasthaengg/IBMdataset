n = int(input())
A = sorted(list(map(int, input().split())))
print(sum(A[-2:-2 * n - 1:-2]))