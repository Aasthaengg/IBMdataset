# coding: utf-8

N, M = map(int,input().split())
A = []
B = []
for i in range(N):
    A.append(list(input()))

for i in range(M):
    B.append(list(input()))
    
w = len(B[0])
flg = False    
for i in range(N-M+1):
    if flg:
        break
    
    for j in range(len(A[0])-len(B[0])+1):
        if flg:
            break
        cnt = 0
        for k in range(M):
            #print(i+k)
            #print(A[i+k][j:j+w], B[i+k])
            #print(k, j,j+w)
            if A[i+k][j:j+w] == B[k]:
                cnt += 1
        if cnt == M:
            flg = True
            break

if flg:
    print('Yes')
else:
    print('No')