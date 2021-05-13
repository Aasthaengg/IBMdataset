N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [B[i] - A[i] for i in range(N)]
K = sum(B) - sum(A)
flag = True
if(K < 0):
    flag = False

if(flag):
    p1 = K
    m2 = K
    for i in range(N):
        if(C[i] == 0):
            pass
        elif(C[i] < 0):
            p1 += C[i]
        elif(C[i] > 0):
            if(C[i] % 2 == 0):
                m2 -= C[i] // 2
            else:
                m2 -= C[i] // 2 + 1
                p1 -= 1
    if(p1 < 0 or m2 < 0):
        flag = False
    else:
        if(p1 == 2*m2):
            flag = True
        else:
            flag = False
    #print(K,p1,m2)
#print(C)
if(flag):
    print('Yes')
else:
    print('No')