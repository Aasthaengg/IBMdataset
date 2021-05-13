c = [list(input()) for _ in range(2)]
ans = "NO"
if c[0][::-1] == c[1]:
    ans = "YES"
print(ans)