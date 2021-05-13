N = int(input())
A = list(map(int,input().split()))

cnt = 0
for n in range(N):
    if n+1 == A[A[n]-1]:
        cnt += 1

print(cnt//2)