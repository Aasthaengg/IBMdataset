s = input()

ans = False
if s.startswith('A'):
    if s.count('C') == 1:
        if 2 <= s.find('C') <= len(s) - 2:
            s = s.replace('A', 'a', 1)
            s = s.replace('C', 'c', 1)
            if s.lower() == s:
                ans = True
print('AC' if ans else 'WA')

