n, a, b = map(int, input().split())
dist = abs(a-b)-1
if dist % 2 != 0:
    ans = dist//2+1
else:
    dist -= 1
    ans = min(a+dist//2+1, n-b+1+dist//2+1)

print(ans)
