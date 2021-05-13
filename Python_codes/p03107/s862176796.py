s = str(input())
c0 = s.count('0')
c1 = s.count('1')
print(2 * min(c0, c1))