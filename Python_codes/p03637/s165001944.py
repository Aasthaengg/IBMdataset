N = int(input())
a = list(input().split())
A = [int(a[i]) for i in range(N)]
count_4 = 0
count_2 = 0
count_o = 0

for i in range(N):
    if A[i] % 4 == 0:
        count_4 += 1
    elif A[i] % 2 == 0:
        count_2 += 1
    else:
        count_o += 1

if count_4 < count_o + (1 if count_2 >= 1 else 0) - 1:
    print('No')
else:
    print('Yes')