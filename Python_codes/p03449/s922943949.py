N = int(input())
A1, A2 = [list(map(int, input().split())) for _ in range(2)]
print(max([sum(A1[:i + 1] + A2[i:]) for i in range(N)]))
