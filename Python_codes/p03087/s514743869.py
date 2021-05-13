import sys

N, Q = map(int, sys.stdin.readline().strip().split())
S = sys.stdin.readline().strip()
ls = len(S)

index = [0 for _ in range(len(S)+1)]
for i in range(len(S)):
    if S[i:i+2] == "AC":
        index[i+1] = 1
for i in range(ls):
    index[i+1] += index[i]

# print(index)

for _ in range(Q):
    l, r = map(int, sys.stdin.readline().strip().split())
    print(index[r-1] - index[l-1])