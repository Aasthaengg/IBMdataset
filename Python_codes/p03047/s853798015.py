n,k = map(int,input().split())
a = 0
for i in range(1,n+1):
    if i+k - 1 <= n:
        a += 1
    else:
        a += 0
print(a)
