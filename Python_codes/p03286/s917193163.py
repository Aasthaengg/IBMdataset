N = int(input())
digits = []
i = 1
while N != 0:
    if N % pow(2,i) == 0:
        digits.append('0')
    else:
        digits.append('1')
        N -= pow(-2,i-1)
    i += 1

if digits:
    print("".join(reversed(digits)))
else:
    print("0")
