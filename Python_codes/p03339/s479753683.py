import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline()

right = S[1:].count("E")
left = 0
ans = [0]*N
ans[0] = right + left
for i in range(1, N):
    if S[i] == "E":
        right = right - 1
    if S[i-1] == "W":
        left = left + 1
    ans[i] = right+left

print(min(ans))