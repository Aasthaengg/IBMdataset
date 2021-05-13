N = int(input())
sw = 0

for i in range(1,9+1):
    if N % i == 0 and N / i <= 9:
        sw = 1
        i = 10

if sw == 1:
    print('Yes')
else:
    print('No')