x, y = input().split()
if x == y:
    ans = "="
elif x < y:
    ans = "<"
else:
    ans = ">"
print(ans)
