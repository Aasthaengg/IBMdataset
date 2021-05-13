import sys
input = lambda: sys.stdin.readline().rstrip()

from itertools import accumulate

N, K = map(int, input().split())

S = input()

num = []

if S[0] == '0':
    num.append(0)

if S[-1] == '1':
    S += '0'
else:
    S += '1'

cnt = 1

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        cnt += 1
    else:
        num.append(cnt)
        cnt = 1

if S[-2] == '0':
    num.append(0)

num = [0] + num

cum_sum = list(accumulate(num))


ans = 0
for i in range(0, len(cum_sum), 2):
    right = i + K * 2 + 1

    if right > len(cum_sum)-1:
        right = len(cum_sum) - 1

    ans = max(ans, cum_sum[right]-cum_sum[i])

print(ans)