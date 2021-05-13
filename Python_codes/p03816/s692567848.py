N = int(input())
A = map(int, input().split())
d = N - len(set(A))
print(N - (d + 1) // 2 * 2)
