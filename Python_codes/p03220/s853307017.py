N = int(input())
T, A = map(int, input().split())
Hs = list(map(int, input().split()))

diff = list(map(lambda x: abs(A - (T - x * 0.006)), Hs))
idx = diff.index(min(diff))
print(idx + 1)
