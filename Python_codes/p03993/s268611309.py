N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
cnt = 0
for i in range(1,N+1):
    ind = A[i]
    if A[ind]==i:
        cnt += 1
print(cnt//2)