a, b = map(int, input().split())
ans = a*b
if len(str(a)) == 2 or len(str(b)) == 2:
    print(-1)
else:
    print(ans)