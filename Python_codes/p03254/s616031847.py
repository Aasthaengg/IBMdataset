N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
cnt=0
for i in range(N):
    if A[i]<=X:
        X-=A[i]
        cnt+=1
    else:
        break
if X>0 and cnt==N:
    cnt-=1
print(cnt)
