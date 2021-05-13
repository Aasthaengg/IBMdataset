import sys

mod = 10**9+7

N,K = map(int,input().split())

A = list(map(int,input().split()))

det = -1###Aのすべての要素が負か否か
for i in range(K):
    if A[i] >= 0:
        det = 1
        break

if det == -1 and K%2 == 1:
    value = 1
    A.sort(reverse = True)
    for i in range(K):
        value *= A[i]
        value %= mod
    print(value)
    sys.exit(0)

A.sort(key = lambda x:abs(x), reverse = True)

###
#print(A[(K-100):K])
#print(A[K:(K+100)])
###

value = 1
sgn = 1
for i in range(K):
    value *= A[i]
    value %= mod
    if A[i] < 0:
        sgn *= -1
    elif A[i] == 0:
        sgn = 0

#print(sgn,value)

if N==K:
    print(value)

elif sgn >=0:
    print(value)
else:
    ###この場合、A[0],...,A[K-1]の中に0はないと断言できることに注意

    X = ['','']###A[K-1],A[K-2],...の中にある絶対値最小の正の数、負の数の絶対値
    num = K
    while (X[0] == '' or X[1] == '') and num > 0:
        #print(A[num])
        num -= 1
        if A[num] > 0 and X[0] == '':
            X[0] = A[num]
        elif A[num] < 0 and X[1] == '':
            X[1] = A[num]
        ###
        #print(X)
        ###
    
    Y = ['','']###A[K], A[k+1],...の中にある絶対値最大の非負の数、負の数
    ###こちらでは0が登場しないとは言えない
    ###前者にだけ0を入れることでカバー
    num = K-1
    while (Y[0] == '' or Y[1] == '') and num < N-1:
        num += 1
        if A[num] > 0 and Y[0] == '':
            Y[0] = A[num]
        elif A[num] < 0 and Y[1] == '':
            Y[1] = A[num]
    
    #print(X)
    #print(Y)

    if X[0] != '' and X[1] != '' and Y[0] != '' and Y[1] != '':
        if abs(X[0]*Y[0]) >= abs(X[1]*Y[1]):
            value *= Y[0]
            value *= pow(X[1],mod-2,mod)
            value %= mod
            print(value)
        else:
            value *= Y[1]
            value *= pow(X[0],mod-2,mod)
            value %= mod
            print(value)

    elif X[1] != '' and Y[0] != '':
        value *= Y[0]
        value *= pow(X[1],mod-2,mod)
        value %= mod
        print(value)
    
    else:
        value *= Y[1]
        value *= pow(X[0],mod-2,mod)
        value %= mod
        print(value)


