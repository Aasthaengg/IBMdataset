a, b, c, d = map(int, input().split())

l = a+b
r = c+d

ans = ''
if l > r:
    ans = 'Left'
elif l == r:
    ans = 'Balanced'
else:
    ans = 'Right'

print(ans)