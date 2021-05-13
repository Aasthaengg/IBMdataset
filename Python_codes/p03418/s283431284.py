# ABC090 D - Remainder Reminder
si = lambda: input()
ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))
n,k=nm()
ans=0

if k==0:
    print(n**2)
    exit()

for i in range(k+1,n+1):
    ans+=(n//i)*(i-k)
    if n%i>=k:
        ans+=n%i-k+1

print(ans)