# E - Payment

N = input().strip()

s = 0
carry = 0
prev = None
for c in reversed(N):
    x = int(c) + carry
    if x > 5 or x == prev == 5:
        if prev == 5:
            x += 1
        s += 10 - x
        carry = 1
    else:
        s += x
        carry = 0
    prev = x
s += carry

print(s)
