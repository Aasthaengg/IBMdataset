s = input()

if s[0:3] == 'KIH':
    s = 'A'+s
elif s[0:4] != 'AKIH':
    print('NO')
    exit(0)
# print(s)

if s[4:5] == 'B':
    s = s[0:4]+'A'+s[4:]
elif s[4:6] != 'AB':
    print('NO')
    exit(0)
# print(s)

if s[5:7] == 'BR':
    s = s[0:6]+'A'+s[6:]
elif s[5:7] != 'BA':
    print('NO')
    exit(0)

# print(s)
# print(s[7:8])
# print(s[7:9])
# print(len(s))
if (s[7:9] == 'RA' and len(s) == 9) or (s[7:8] == 'R' and len(s) == 8):
    print('YES')
else:
    print('NO')
