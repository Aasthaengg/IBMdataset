N = input()

cnt = 0
for i in range(len(N)-1):
    if N[i] == N[i+1]:
        cnt += 1
    else:
        cnt = 0
    if cnt == 2:
        print('Yes')
        break
else:
    print('No')