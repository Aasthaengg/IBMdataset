k, t = map(int, input().split())
a = list(map(int, input().split()))
print(max(0, 2 * max(a) - k - 1))