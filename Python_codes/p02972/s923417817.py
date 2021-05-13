n=int(input())
a=list(map(int,input().split()))

hako=[0]*n
for i in range(n):
    # print(n-i-1, sum(hako[n-i-1:n:n-i]))
    if (sum(hako[n-i-1:n:n-i])%2)!=a[n-i-1]:
        hako[n-i-1]+=1
# print(hako)

ans=[]
for i in range(n):
    if hako[i]==1:
        ans.append(str(i+1))

print(len(ans))
if len(ans)!=0:
    print(' '.join(ans))
