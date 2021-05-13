a, b, x = map(int, input().split())
ans = 'NO'
if x >= a and a + b >= x:
    ans = 'YES'
print(ans)