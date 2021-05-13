x, y, z = map(int,input().split())
ans = abs(y-z)-x
print(ans) if ans > 0 else print(0)