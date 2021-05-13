n,k,s = map(int,input().split())

if n>k:
    ans = [s for i in range(k)]
    nokori = n-k
    for i in range(nokori):
        if s==10**9:
            ans.append(1)
        else:
            ans.append(10**9)
else:
    ans = [s for i in range(k)]
print(*ans)
