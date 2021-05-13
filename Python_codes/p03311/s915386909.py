n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    a[i]-=(i+1)
a.sort()

a_sum=[a[0]]
a_minus_sum=[-a[0]]

for i in range(1,n):
    a_sum.append(a[i]+a_sum[-1])
    a_minus_sum.append(-a[i]+a_minus_sum[-1])

ans=min(a_sum[-1]-a[0]*n,a_minus_sum[-1]+a[-1]*n)

for g in range(1,n-1):
    ans=min(a[g]*(-n+2*g+1)+a_sum[-1]-a_sum[g]+a_minus_sum[g-1],ans)

print(ans)