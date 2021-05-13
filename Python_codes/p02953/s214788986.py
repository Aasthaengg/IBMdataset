N = int(input())
hhh = list(map(int, input().split()))
flag = True
for i in range(N - 1):
    if hhh[i] < hhh[i + 1]:
        flag = True
    elif hhh[i] == hhh[i + 1]:
        pass
    elif (hhh[i] == hhh[i + 1] + 1) and flag:
        flag = False
    else:
        print('No')
        exit()
print('Yes')
