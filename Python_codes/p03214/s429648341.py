import sys

read = sys.stdin.read

N, *a = map(int, read().split())
ave = sum(a)
a = [abs(i * N - ave) for i in a]

print(a.index(min(a)))
