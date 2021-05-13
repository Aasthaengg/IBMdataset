INPUT = list(map(int, input().split()))

N = INPUT[0]
A = INPUT[1]
B = INPUT[2]

total_all = 0
for i in range(N+1):
    total_epoch = sum([int(j) for j in str(i)])
    if total_epoch >= A and total_epoch <= B:
        total_all += i
print(total_all)