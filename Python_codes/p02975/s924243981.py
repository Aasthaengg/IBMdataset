N = int(input())
A = list(map(int,input().split()))
X = set(A)
if len(X) == 1:
    if 0 in X:
        ans = 1
    else:
        ans = 0
elif len(X) == 2:
    if 0 in X:
        Y = list(X)
        if A.count(Y[0]) * 2 == A.count(Y[1]):
            ans = 1
        else:
            ans = 0
    else:
        ans = 0
elif len(X) == 3:
    Y = list(X)
    if A.count(Y[0]) == A.count(Y[1]) == A.count(Y[2]):
        ans = 1
        for i in range(40):
            Z = list(map(lambda x: x % 2,Y))
            Y = list(map(lambda x: x // 2,Y))
            Z.sort()
            #print(Z)
            if Z != [0,1,1] and Z != [0,0,0]:
                ans = 0
                break
    else:
        ans = 0
elif len(X) >= 4:
    ans = 0
if ans == 0:
    print('No')
else:
    print('Yes')