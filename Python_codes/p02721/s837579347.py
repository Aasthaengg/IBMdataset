from collections import deque
N, K, C = map(int, input().split())
S = input()

fastest = deque([])
latest = deque([])


date = 1

for work_days in range(K):
    while S[date - 1] == 'x':
        date += 1
    fastest.append(date)
    date += C + 1

date = 1

for work_days in range(K):
    while S[- date] == 'x':
        date += 1
    latest.append(N - (date - 1))
    date += C + 1

for i in range(K):
    f = fastest.popleft()
    l = latest.pop()
    if f == l:
        print(f)