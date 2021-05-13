import sys
input = sys.stdin.readline

h, a = list(map(int, input().split()))

k = h // a

if h % a == 0:
    print(k)
else:
    print(k+1)