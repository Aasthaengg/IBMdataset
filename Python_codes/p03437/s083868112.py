X, Y = map(int, input().split())
a = X / Y
if a == int(a):
    ans = -1
else:
    ans = X
print(ans)