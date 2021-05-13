n,*a = map(int, open(0).read().split())
ans = [0] * n
for i in range(1,n+1):
    if i % 2 == 1:
        ans[i//2] = a[-i]
    else:
        ans[-(i//2)] = a[-i]
print(*ans)