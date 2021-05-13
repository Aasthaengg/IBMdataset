
X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))

P.sort()
Q.sort()
cand = P[-X:] + Q[-Y:] + R
cand.sort()
print(sum(cand[-(X + Y):]))
