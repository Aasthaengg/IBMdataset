N = int(input())

ans = 1
for i in range(2,N+1):
    tmp = 2
    while i**tmp<=N:
        ans = max(ans,i**tmp)
        tmp += 1
print(ans)