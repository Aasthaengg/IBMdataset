N = int(input())
hhh = list(map(int, input().split()))
for i in range(N - 2, -1, -1):
    if hhh[i] <= hhh[i + 1]:
        pass
    elif hhh[i] - hhh[i + 1] == 1:
        hhh[i] -= 1
    else:
        print('No')
        exit()
print('Yes')
