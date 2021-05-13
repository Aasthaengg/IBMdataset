N, K = map(int, input().split())
A = list(map(int, input().split()))
a=[0]*200001
cnt=0
for i in range(N):
    if a[A[i]]==0:
        cnt+=1
    a[A[i]]+=1
a.sort(reverse=True)
sum=0
for i in range(cnt-K):
    sum+=a[cnt-i-1]

print(sum)