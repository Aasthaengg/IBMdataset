a, b, x = map(int, input().split())

# ans = 0
bx = b//x + 1
ax = (a-1)//x + 1
ans = bx - ax
print(ans)