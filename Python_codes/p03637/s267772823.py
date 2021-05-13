N = int(input())
a = list(map(int, input().split()))
kisu = 0
gusu = 0
num_4 = 0

for i in range(N):
    if a[i] % 2 == 1:
        kisu += 1
    elif a[i] % 4 == 0:
        num_4 += 1
    else:
        gusu += 1
if gusu != 0:
    kisu += 1

print('Yes' if kisu <= num_4+1 else 'No')