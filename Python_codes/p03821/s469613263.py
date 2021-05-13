n=int(input())
ab=[map(int,input().split()) for _ in range(n)]
a,b = [list(i) for i in zip(*ab)]

s=0
for i in range(n):
    if (a[n-1-i]+s)%b[n-1-i]==0:
        continue
    else:
        c=b[n-1-i]-((a[n-1-i]+s)%b[n-1-i])
        s+=c
print(s)