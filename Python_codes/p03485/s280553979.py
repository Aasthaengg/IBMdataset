a, b = map(int,input().split())
ans = a + b
if ans % 2 == 1:
    ans += 1
ans //= 2
print(ans)