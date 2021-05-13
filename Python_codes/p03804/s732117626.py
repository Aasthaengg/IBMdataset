I = input().split()
N = int(I[0])
M = int(I[1])
## input A and B ##
A = [["" for i in range(N)] for i in range(N)]
B = [["" for i in range(M)] for i in range(M)]
for i in range(N):
    A[i] = list(input())
for i in range(M):
    B[i] = list(input())

# print(A,B)

# print([ A_i[0:2] for A_i in A[0:2] ])

# print( B == [ A_i[0:2] for A_i in A[0:2] ]  )

EQ_flag = 0
for i in range(N+M+1):
    for j in range(N+M+1):
        if ( B == [ A_i[i:i+M] for A_i in A[j:j+M] ] ):
            EQ_flag = 1
            break

if(EQ_flag):
    print('Yes')
else:
    print('No')