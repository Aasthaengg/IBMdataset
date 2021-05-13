import sys
input = sys.stdin.readline

X, N = map(int, input().split())
p = list(map(int, input().split()))
st = set(p)
for i in range(X+1):
    if X - i not in st:
        print(X - i)
        break
    if X + i not in st:
        print(X + i)
        break
