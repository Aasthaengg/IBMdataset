N,K = map(int,input().split(' '))
A = list(map(int,input().split(' ')))
cnt = 0
for k in range(K,N):
    if A[k] > A[cnt]:
        print("Yes")
    else:
        print("No")
    cnt += 1
