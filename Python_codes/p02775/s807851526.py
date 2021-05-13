s = input()

ans = 0
carry = 0
for i in range(len(s) - 1, -1, -1):
    c = int(s[i])
    if c + carry < 5:
        ans += c + carry
        carry = 0
    elif c + carry == 5:
        if i > 0 and int(s[i - 1]) >= 5:
            ans += 5
            carry = 1
        else:
            ans += 5
            carry = 0
    else:
        ans += 10 - c - carry
        carry = 1
if carry:
    ans += 1
print(ans)
