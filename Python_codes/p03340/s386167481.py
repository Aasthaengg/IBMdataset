n = int(input())
a = tuple(map(int,input().split()))

res = 0
p = 0
cnt = 0

for i in range(n):

    while cnt < n:
        if p&a[cnt] == 0:
            p = p^a[cnt]
            cnt += 1
        else:
            break
    
    p = p^a[i]
    res += cnt-i

print(res)