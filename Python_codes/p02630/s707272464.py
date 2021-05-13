N = int(input())
A = list(map(int,input().split()))
Q = int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i],C[i] = map(int, input().split())

S = sum(A)
num_dict = {i:0 for i in range(1,100001)}
for i in range(N):
    num_dict[A[i]] += 1

S_dif = 0
for i in range(Q):
    S_dif = (C[i] - B[i])*num_dict[B[i]]
    num_dict[C[i]] += num_dict[B[i]]
    num_dict[B[i]] = 0
    S += S_dif
    print(S)