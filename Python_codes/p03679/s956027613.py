x, a, b = map(int, input().split())
ans = 'dangerous'
if b-a <= 0:
    ans = 'delicious'
elif (b-a) <= x:
    ans = 'safe'
print(ans)