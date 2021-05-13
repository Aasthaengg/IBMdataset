N = int(input())
A = sorted(list(map(int,input().split())))
B = [0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i] = B[i-1]+A[i-1]
cnt = 1
for i in range(N-2,-1,-1):
    if A[i+1]<=2*B[i+1]:
        cnt += 1
    else:
        break
print(cnt)