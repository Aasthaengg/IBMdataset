from sys import stdin
input = stdin.readline
X, K, D = map(int, input().split())
A=int((K-X/D)/2)
if 0<=A and A<=K:print(min(abs(-K*D+2*A*D+X),abs(-K*D+2*(A+1)*D+X)))
else:print(min(abs(X+K*D),abs(X-K*D)))