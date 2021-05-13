n = int(input())
lis = [int(input()) for _ in range(n)]

lis = sorted(lis)
t = sum(lis)

if t % 10 != 0:
    print(t)
    exit()
else:
    tmp = [0]*n
    ans = 0
    for i in range(n):
        tmp[i] = t - lis[i]
    
    for j in range(n):
        if tmp[j] % 10 != 0:
            ans = max(ans, tmp[j])

print(ans)