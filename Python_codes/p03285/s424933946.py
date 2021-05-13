N = int(input())
flag = 0
for i in range(N//4 + 1):
    for j in range(N//7 + 1):
        if N == (4*i + 7*j):
            flag = 1
if flag == 1:
    print('Yes')
else:
    print('No')