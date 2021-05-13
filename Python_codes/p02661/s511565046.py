import sys
input = sys.stdin.readline

def med(s: list):
    n = len(s)
    s = sorted(s, reverse = True)
    return s[(n + 1) // 2 - 1] if n & 1 else (s[n // 2] + s[n // 2 - 1]) / 2

n = int(input())
a, b = [], []
for i in range(n):
    aa, bb = map(int, input().split())
    a.append(aa), b.append(bb)
ma, mb = med(a), med(b)
print(int((mb - ma) + 1) if n & 1 else int((mb - ma) * 2 + 1))