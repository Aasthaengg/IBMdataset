N = int(input())
A = list(map(int,input().split()))
cnt = 0
cur = 0
for i in range(1,N):
    if A[i]==A[cur]:
        continue
    else:
        cnt += (i-cur)//2
        cur = i
cnt += (N-cur)//2
print(cnt)