N, K, C = map(int, input().split())
S = input()

work_days_early = []
counter = 0
i = 0
while i < N:
    if S[i] == 'o':
        work_days_early.append(i+1)
        counter += 1
        if counter >= K:
            break
        i += C
    i += 1

work_days_late = []
counter = 0
i = N-1
while i >= 0:
    if S[i] == 'o':
        work_days_late.append(i+1)
        counter += 1
        if counter >= K:
            break
        i -= C
    i -= 1
work_days_late.reverse()

work_days_necessary = []
for day1, day2 in zip(work_days_early , work_days_late):
    if day1 == day2:
        work_days_necessary.append(day1)

print(*work_days_necessary, sep = '\n')