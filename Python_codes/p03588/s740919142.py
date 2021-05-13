N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
A.sort()
print(sum(A[-1]))