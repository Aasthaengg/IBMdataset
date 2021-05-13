s = list(input())
odd = set(s[::2])
even = set(s[1::2])
if 'L' in odd or 'R' in even:
    print("No")
else:
    print('Yes')
