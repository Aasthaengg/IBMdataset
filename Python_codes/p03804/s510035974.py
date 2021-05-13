N,M = map(int,input().split())
a = []
b = []

for _ in range(N):
    a.append(input())
for _ in range(M):
    b.append(input())
flg = True
for i in range(N):
    for j in range(N-M+1):
        #print(a[i][j:j+(M-1)])
        if a[i][j:j+M] == b[0]:
            if M == 1:
                print('Yes')
                exit()
            else:
                for k in range(1,M):
                    if a[k][j:j+M] != b[k]:
                        flg = False
                        break
                if flg:
                    print('Yes')
                    exit()
                else:
                    flg = True
print('No')