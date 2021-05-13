w, a, b = map(int,input().split())
ans = 0
if b+w < a:
    ans = a - (b+w)
if a+w < b:
    ans = b - (a+w)
print(ans)