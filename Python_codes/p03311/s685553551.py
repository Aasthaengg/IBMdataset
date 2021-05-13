n=int(input())
a=list(map(int, input().split()))

a_new=[0]*n
for i in range(n):
    a_new[i]=a[i]-i
a_new.sort()
b=a_new[(n-1)//2]
ans=0
for i in range(n):
    ans+=abs(a[i]-i-b)

print(int(ans))
