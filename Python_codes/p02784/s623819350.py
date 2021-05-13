import sys
input = sys.stdin.buffer.readline
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

h, n = MAP()
a = LIST()

print('Yes') if h <= sum(a) else print('No')