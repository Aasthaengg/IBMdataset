N,K,Q=map(int,input().split())
A = []
for _ in range(Q):
    A.append(int(input()))#縦入力
Nlist = []
for i in range(N):
    Nlist.append(K-Q)
for j in range(0,Q):
    Nlist[A[j]-1] += 1
for k in range(0,N):
    if Nlist[k]>=1:
        print("Yes")
    else:
        print("No")