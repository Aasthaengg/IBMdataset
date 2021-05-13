n=int(input())
a=list(map(int,input().split()))
cnt = [0] * (n+1)

for i in range(n):
    cnt[a[i]]+=1

Ans = 0
for i in range(1,n+1):
    Ans += cnt[i] * (cnt[i]-1) // 2

for i in range(n):
    ans = Ans - cnt[a[i]]
    print(ans+1)