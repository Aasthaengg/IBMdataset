import sys


def input():
    return sys.stdin.readline().strip()


N = int(input())
S = []
T = []
for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
X = input()
A = S.index(X)
print(sum(T[A + 1 :]))
