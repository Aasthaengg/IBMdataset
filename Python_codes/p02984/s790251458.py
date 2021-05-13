n = int(input())
a = list(map(int,input().split()))
x = 0
for i in range(n):
    x = a[i] - x
ans = []
ans.append(x)
for i in range(n-1):
    ans.append((a[i]-ans[-1]//2)*2) 
print(*ans)