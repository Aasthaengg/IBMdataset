
N,M = map(int,input().split())

lis = [0] * N
for i in range(M):

    a,b = map(int,input().split())

    lis[a-1] += 1
    lis[b-1] += 1

flag = True
for i in range(N):

    if lis[i] % 2 == 1:
        flag = False
        break

if flag:
    print ("YES")
else:
    print ("NO")
