import sys
N = int(input())
a = list(map(int, input().split()))
num, cut = 0, 0

if N == 1:
    print(1)
    sys.exit()

for i in range(N-1):
    if a[i] == a[i+1]:
        continue
    if a[i] < a[i+1] and num == 0:
        num  = 1
        cut += 1
    elif a[i] > a[i+1] and num == 0:
        num = -1
        cut += 1
    elif num == 1 and a[i] > a[i+1]:
        if i == N-2:
            cut += 1
        num = 0
    elif num == -1 and a[i] < a[i+1]:
        if i == N-2:
            cut += 1
        num = 0
print(cut)
        
