X, A, B = map(int, input().split())

if B - A > X:
    ans = 'dangerous'
elif B - A > 0:
    ans = 'safe'
else:
    ans = 'delicious'
print(ans)
