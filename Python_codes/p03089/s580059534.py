N = int(input())
b = list(map(int, input().split()))
for i in range(N):
    b[i] -= 1
lis = []
for i in range(N):
    flg = False
    for j in reversed(range(N-i)):
        if b[j] == j:
            lis.append(j+1)
            del b[j]
            flg = True
            break
    if flg == False:
        print(-1)
        exit()
for i in reversed(range(N)):
    print(lis[i])
