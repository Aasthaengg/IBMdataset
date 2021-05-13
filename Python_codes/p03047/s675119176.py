N,K = map(int,input().rstrip().split(' '))

count = 0
flag = 0

for i in range(N):
    flag = 0
    for j in range(K):
        if i + j < N:
            pass
        else:
            flag = 1

    if flag == 0:
        count += 1
    else:
        break

print(count)