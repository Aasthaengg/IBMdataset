import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
W = [0] * N
E = [0] * N

cnt = 0
for i in range(1, N):
    if S[i-1] == "W":
        cnt += 1
        W[i] = cnt
    else:
        W[i] = cnt
cnt = 0
for i in reversed(range(N-1)):
    if S[i+1] == "E":
        cnt += 1
        E[i] = cnt
    else:
        E[i] = cnt

min = float("inf")
for i in range(N):
    if W[i] + E[i] < min:
        min = W[i] + E[i]
print(min)