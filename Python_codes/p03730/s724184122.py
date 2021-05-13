a,b,c = map(int, input().split())
ans = "NO"
for x in range(b+1):
    if (a*x) % b == c:
        ans = "YES"
        break
print(ans)