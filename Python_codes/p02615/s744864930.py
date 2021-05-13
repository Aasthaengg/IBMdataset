N = int(input())
A = sorted(list(map(int,input().split())),reverse=True)
cnt = A[0]
k = (N+1)//2-1
for i in range(1,1+k):
    cnt += 2*A[i]
if N%2==1:
    cnt -= A[k]
print(cnt)