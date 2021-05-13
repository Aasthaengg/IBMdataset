import copy
n,k = map(int,input().split())
ai = [int(i) for i in input().split()]

#old_ai = ai
cnt = 0

aij = [[0 for i in range(n)] for j in range(2)]
aij[0] = ai

while 1 == 1:
    li = [0]*(n+1)
    for i in range(n):
        li[max(0,i-aij[0][i])] += 1
        li[min(n,i+1+aij[0][i])] -= 1
        #print(li)
    #print(li)
    tmp = 0
    for i in range(n):
        if i == 0:
            aij[1][i] = li[i]
            tmp += aij[1][i]
        else:
            aij[1][i] = li[i] + aij[1][i-1]
            tmp += aij[1][i]
    #print(rui)
    if aij[1] == aij[0]:
        print(*aij[1])
        exit()
        break
    cnt += 1
    if cnt == k:
        print(*aij[1])
        exit()
    for i in range(n):
        aij[0][i] = aij[1][i]