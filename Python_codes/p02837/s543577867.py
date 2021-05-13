import itertools
N = int(input())
lis_hl = list(itertools.product('01',repeat = N))
#1正直者 　0不親切
A = []
X = []
for i in range(N):
    A.append(int(input()))
    Y =[]
    for j in range(A[-1]):
        Y.append(list(map(int,input().split())))
    X.append(Y)
honesty = 0
for hl in lis_hl:#honesty laier list
    flag = 0
    for i in range(N):#人について探査
        if flag == 0:
            is_hl = hl[i]# これから証言するひとは正直者か
            if is_hl == '1':
                
                for xi in X[i]:#証言を全探索
                    if xi[1] != int(hl[xi[0]-1]):
                        flag = 1
                        break
    if flag == 0:
        honesty = max(honesty,hl.count('1'))
print(honesty)
