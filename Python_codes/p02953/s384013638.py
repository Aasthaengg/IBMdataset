from sys import exit
n = int(input())
hh = list(map(int, input().split()))

for i in range(n-1,0,-1):
    if hh[i] >= hh[i-1]:
        continue
    else:
        hh[i-1] -= 1
        if hh[i] >= hh[i-1]:
            continue
#         print(i)
        print('No')
        exit()
print('Yes')