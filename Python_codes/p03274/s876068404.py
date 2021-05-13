N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans =[]
if arr[0]>0:
    ans.append(arr[K-1])

if arr[-1]<0:
    ans.append(abs(arr[-1*(K)]))

for i in range(N-K+1):
    if arr[i]*arr[i+K-1]<=0:
        left =2*abs(arr[i])+abs(arr[i+K-1])
        right=2*abs(arr[i+K-1])+abs(arr[i])
        ans.append(min(left,right))

print(min(ans))