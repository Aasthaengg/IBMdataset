a, b = map(int, input().split())

if b < a:
    ans = a -1
if b >= a:
    ans = a

print(ans)