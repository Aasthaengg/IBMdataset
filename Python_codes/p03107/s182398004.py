S = input()

zero_count = int(S.count('0'))
one_count = int(S.count('1'))

print(min(zero_count, one_count)*2)
