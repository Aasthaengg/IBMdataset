n=int(input())
a=list(map(int,input().split()))
left_ruiseki=[a[0]]
for i in range(1,n):
    left_ruiseki.append(left_ruiseki[i-1]+a[i])
a.reverse()
right_ruiseki=[a[0]]
for i in range(1,n):
    right_ruiseki.append(right_ruiseki[i-1]+a[i])

ans=10000000000
for i in range(n-1):
    ans=min(ans,abs(left_ruiseki[i]-right_ruiseki[-i-2]))
print(ans)