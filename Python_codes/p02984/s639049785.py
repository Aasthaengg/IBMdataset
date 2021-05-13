n = int(input())
a = list(map(int, input().split()))
sma = sum(a)
ans = []
ans.append(sma- 2*sum(a[1:n-1:2]))
for i in range(n-1):
    val = 2*a[i]-ans[i]
    ans.append(val)

for i in ans:
    print(i,end=" ")