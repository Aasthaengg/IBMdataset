s = input()
if 'C' in s:
    c = s.index("C")
    if "F" in s[c:]:
        print('Yes')
        exit()
print('No')
