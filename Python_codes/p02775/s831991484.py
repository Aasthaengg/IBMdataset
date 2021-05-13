N = reversed("0" + input())
digit = next(N)
total = 0
carry = 0
for nextdigit in N:
    digit = int(digit) + carry
    if digit < 5:
        total += digit
        carry = 0
    elif digit == 5:
        if int(nextdigit) < 5:
            total += digit
            carry = 0
        else:
            total += 10 - digit
            carry = 1
    else:
        total += 10 - digit
        carry = 1
    digit = nextdigit

print(total + carry)
