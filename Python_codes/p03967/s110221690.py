s = input()
max_p = len(s) // 2
if max_p <= s.count('p'):
    print(0)
else:
    print(max_p - s.count('p'))
