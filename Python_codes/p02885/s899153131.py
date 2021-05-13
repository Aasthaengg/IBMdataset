a ,b = map(int,input().split())
ans = 0
if a > 2 * b:
    ans = a - 2*b
else:
    ans = 0
print(ans)
