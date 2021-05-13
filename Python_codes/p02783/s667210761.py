import sys
input = sys.stdin.buffer.readline
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

h, a = MAP()
print(h//a) if h % a == 0 else print(1 + h//a)