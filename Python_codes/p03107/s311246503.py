s = input()
one = s.count('1')
zero = s.count('0')

print(len(s) - abs(one - zero))
