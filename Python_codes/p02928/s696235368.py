n,k=map(int,input().split())
a=list(map(int,input().split()))

inter = 0
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            inter += 1
outer = 0
for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            outer += 1

ans = inter*k + outer*k*(k-1)//2
ans %= 10**9+7
print(ans)