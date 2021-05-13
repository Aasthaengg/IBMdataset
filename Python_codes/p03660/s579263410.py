from collections import deque
n = int(input())
ab = [[] for i in range(n)]

for i in range(n-1):
    a,b = map(int,input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

fnc = deque()
snk = deque()

fnc.appendleft(0)
snk.appendleft(n-1)

check = [0]*(n)

check[0] = 1
check[n-1] = 1

fnc_num = 0
snk_num = 0

while len(fnc) > 0 or len(snk) > 0:
    for i in range(len(fnc)):
        tmp = fnc.popleft()
        for j in range(len(ab[tmp])):
            if check[ab[tmp][j]] == 0:
                fnc_num += 1
                check[ab[tmp][j]] = 1
                fnc.append(ab[tmp][j])
                
    for i in range(len(snk)):
        tmp = snk.popleft()
        for j in range(len(ab[tmp])):
            if check[ab[tmp][j]] == 0:
                snk_num += 1
                check[ab[tmp][j]] = 1
                snk.append(ab[tmp][j])
                
    #fnc.popleft()
    #snk.popleft()
    
if fnc_num > snk_num:
    print('Fennec')
else:
    print('Snuke')