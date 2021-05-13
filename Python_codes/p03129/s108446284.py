a, b = map(int, input().split())
M = int( (a - 1) / 2) + 1
if M >= b:
    ans = 'YES'
else:
    ans = 'NO'
print(ans)