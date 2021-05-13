n = int(input())
k = int(input())


ans = 100000001
for i in range(1<<n):
    tmp = 1
    
    for j in range(n):
        if (i>>j) & 1:
            tmp *= 2
        else:
            tmp += k
    
    ans = min(ans, tmp)

print(ans)