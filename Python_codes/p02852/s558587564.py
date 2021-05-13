import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = input()
if '1'*M in S:
    print(-1)
    exit()
nums = []
cur = N
min_loc = N
for i in range(N)[::-1]:
    if cur-i > M:
        nums.append(cur-min_loc)
        cur = min_loc
    if S[i] == '0':
        min_loc = min(min_loc, i)
if cur > 0:
    nums.append(cur)
print(' '.join(map(str, nums[::-1])))
