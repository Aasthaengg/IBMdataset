n, k , s = map(int,input().split())
x = s//2
y = s-x
if s==10**9:
    m = s-1
else:
    m = 10**9
print(*[s for _i in range(k)]+[m for _j in range(n-k)])