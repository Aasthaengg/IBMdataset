str_n = input()
digits = [int(c) for c in str_n]

if sum(digits[1:]) == 9 * (len(digits) - 1):
    print(sum(digits))
else:
    print(digits[0] + 9 * (len(digits) - 1) - 1)
