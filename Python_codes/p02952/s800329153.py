n = int(input())
ans = 0
i = 1
for _ in range(1,n+1):
    if i > n: break
    if len(str(i))%2!=0: 
        ans += 1
        i += 1
    else:
        i *= 10
print(ans)