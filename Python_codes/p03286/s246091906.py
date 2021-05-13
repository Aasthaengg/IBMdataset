n = int(input())

def helper(x):
    if x == 0:
        return []
    r = x % (-2)
    return [r] + helper((x - r) // (-2))


tmp = helper(n)

ans = ''
carry = 0
for x in tmp:
    xx = x + carry
    if xx == -1:
        ans += '1'
        carry = 1
    elif xx == 0:
        ans += '0'
        carry = 0
    elif xx == 1:
        ans += '1'
        carry = 0
if carry:
    ans += '1'

if n == 0:
    print(0)
else:
    ans = str(int(ans[::-1]))
    print(ans)
