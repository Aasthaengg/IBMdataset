#import numpy as np

N=int(input())
AAA=input().split()
#A = np.array([int(i) for i in AAA])
A = [int(i) for i in AAA]

max_abs_index = -1

indexbox = [[-1 for i in range(2)] for j in range(2*N)]
i=0
j=0
c=-1
max_abs_index=max(range(N), key=lambda i: abs(A[i]))
while(0!=c):
    max_abs_index=max(range(N), key=lambda i: abs(A[i]))
#    print('here')
    indexbox[i][0] = A[max_abs_index]
    indexbox[i][1] = max_abs_index
    c = A[max_abs_index]
    if indexbox[i][0] < 0:
        for p in range(max_abs_index+1):
            A[p] =0
    if indexbox[i][0] > 0:
        for p in range(max_abs_index,N):
            A[p] =0
    i = i+1
#    print(indexbox)
#    print(A)
#    print(c)
#    print(i)
#print(A)    

if i == 1:
    print(0)
else:
    a = indexbox[i-2][1]
#    print(indexbox)
 #   print(a)
    if (a == 0 and indexbox[i-2][0]>0) or (a == N-1 and indexbox[i-2][0] < 0):
        pp=2*N-2
    else:
        pp = 2*N-4
    print(pp)
    if indexbox[i-2][0] > 0:
 #       print('positive')
        for j in range(a,N-1):
            print(j+1, j+2)
            print(j+1, j+2)
        for j in range(a,1,-1):
            print(j, j-1)
            print(j, j-1)
    else:
  #      print('negative')
        for j in range(a+1,N-1):
            print(j+1, j+2)
            print(j+1, j+2)
        for j in range(a+1,1,-1):
            print(j, j-1)
            print(j, j-1)
        
    


