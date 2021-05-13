
X, Y, A, B, C = map(int, input().split())
P = sorted(map(int, input().split()))
Q = sorted(map(int, input().split()))
R = sorted(map(int, input().split()))

cand = sorted(P[-X:] + Q[-Y:] + R)
print(sum(cand[-X-Y:]))
