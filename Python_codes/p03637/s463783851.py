N = int(input())
arr = list(map(int, input().split()))
four = 0
two = 0
for i in arr:
    if i % 4 == 0:
        four += 1
    elif i % 2 == 0:
        two += 1
if 2*four+1 == N:
    print('Yes')
    exit()
N -= four * 2
if N <= two:
    print('Yes')
else:
    print('No')