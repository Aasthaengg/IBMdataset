import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = n - sum(list(map(int, input().split())))
print(d if d >= 0 else -1)