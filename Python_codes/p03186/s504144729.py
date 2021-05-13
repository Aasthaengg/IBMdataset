a, b, c = map(int, input().split())
if a+b+1 <= c:
    ans = 2*b+a+1
else:
    ans = b + c
print(ans)