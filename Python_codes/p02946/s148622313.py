k, x = map(int, input().split())
MAX = 1000000
MIN = -1000000
res = list(range(max(x-k+1, MIN), x)) + list(range(x, min(x+k, MAX)))
print(" ".join(list(map(str, res))))