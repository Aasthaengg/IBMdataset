n = int(input())
a, b, c = [list(map(int, input().split())) for i in [0]*3]
ans=0
for i in range(n-1):
    if a[i]+1==a[i+1]:
        ans+=c[a[i]-1]
print(sum(b)+ans)