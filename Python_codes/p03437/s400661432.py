x, y = map(int, input().split())

if x == y: print(-1)
elif (x/y).is_integer(): print(-1)
else: print(x)
