n,c,k = map(int,input().split())
t = list(int(input()) for i in range(n))
t.sort()
ans = 0
i = 0
while i < n:
    a = t[i]
    j = i + 1
    z = 1
    for j in range(i+1,min(i+c,n)):
        if a+k >= t[j]:
            z += 1
        else:
            break
    i += z
    ans += 1
print(ans)