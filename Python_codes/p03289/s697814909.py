import re
s = input()
pattern = 'A[a-z]+C[a-z]+'

result = re.fullmatch(pattern, s)
# print(result)

if result == None:
    print('WA')
else:
    print('AC')

# if s[0] != 'A':
#     print('WA')
# elif s[1].isupper or s[-1].isupper:
#     print('WA')
# elif s.count('C') != 1:
#     print('WA')
# elif :
