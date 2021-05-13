s = input()
num = s.count('0')
print(2 * min(num, len(s) - num))