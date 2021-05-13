s = input()

s1 = ''.join(s.split('A'))
s2 = ''.join('AKIHABARA'.split('A'))

if s1 == s2 and not 'AA' in s and not 'KA' in s and not 'IA' in s:
    print('YES')
else:
    print('NO')
