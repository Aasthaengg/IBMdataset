n = int(input())
A = [0] + list(map(int, input().split()))

ans=0
for i in range(1,n+1):
    if A[i]<i:
        #既にチェック済み
        continue
    if i==A[A[i]]:
        ans+=1

print(ans)