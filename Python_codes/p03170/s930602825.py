n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
dp=[0]*(k+1)
for i in range(a[0]):
    dp[i]="s"
for u in a:
    dp[u]="f"
for i in range(a[0]+1,k+1):
    if dp[i]==0:
        for u in a:
            if i<u:
                continue
            else:
                if dp[i-u]=="s":
                    dp[i]="f"
                    break
        else:
            dp[i]="s"
if dp[k]=="f":
    print("First")
else:
    print("Second")