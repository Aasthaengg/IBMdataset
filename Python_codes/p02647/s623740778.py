import copy
n,k = map(int,input().split())
ai = [int(i) for i in input().split()]

old_ai = ai
cnt = 0

while 1 == 1:
    old_ai = copy.deepcopy(ai)
    li = [0]*(n+1)
    for i in range(n):
        li[max(0,i-ai[i])] += 1
        li[min(n,i+1+ai[i])] -= 1
        #print(li)
    #print(li)
    rui = [0]*n
    tmp = 0
    for i in range(n):
        if i == 0:
            ai[i] = li[i]
            tmp += ai[i]
        else:
            ai[i] = li[i] + ai[i-1]
            tmp += ai[i]
    #print(rui)
    if ai == old_ai:
        print(*ai)
        exit()
        break
    cnt += 1
    if cnt == k:
        print(*ai)
        exit()
    old_ai = ai