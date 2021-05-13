# coding: utf-8

N = int(input())
D = []
for i in range(N):
    s, p = map(str,input().split())
    p = int(p)
    shop = [s, p, i+1]
    D.append(shop)

D.sort(key=lambda x:x[0])
#print(D[0])
#print(D[1])
T_ = [D[0]]
flg = True
A = []
for i in range(N-1):
    #print(T_)
    if D[i][0] == D[i+1][0]:
        T_.append(D[i+1])
    else:
        T_.sort(key=lambda x:x[1], reverse=True)
        A = A + T_
        T_ = [D[i+1]]
        flg = False
        #print('hoge')

if len(T_) > 0:
    T_.sort(key=lambda x:x[1], reverse=True)
    A = A + T_
#print(A)
for l in A:
    print(l[2])