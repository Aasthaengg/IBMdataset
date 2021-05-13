from itertools import accumulate

N = int(input())
S = input()

if N == 2:
    if S == '#.':
        print(1)
    else:
        print(0)
    exit()

s = [1 if i == '#' else 0 for i in S]
a = list(accumulate(s))
b = list(reversed(list(accumulate(reversed(s)))))
answer = N
for i in range(1, N - 1):
    tmp = a[i] + N - i - 1 - b[i]
    if tmp < answer:
        answer = tmp

answer = min(answer, a[-1], N - a[-1])
print(answer)