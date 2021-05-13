N = int(input())

checkpoint = 0
summation = 0

for i in range(1, N+1):
    checkpoint = i
    summation = summation + checkpoint
    if summation >= N:
        break

unn = summation - N
for a in range(1, checkpoint+1):
    if a != unn:
        print(a)