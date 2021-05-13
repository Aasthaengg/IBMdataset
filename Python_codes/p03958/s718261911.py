K, T = map(int, input().split())
A = sorted(list(map(int, input().split())))
print(max((2 * A[-1]) - (K + 1), 0))
