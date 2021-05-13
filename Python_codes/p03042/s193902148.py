def check_my(string):
    if 1 <= int(string) <= 12:
        return 'YorM'
    else:
        return 'Y'

s = input()
my_set = (check_my(s[0:2]), check_my(s[2:4]))
if my_set == ('YorM', 'YorM'):
    print('AMBIGUOUS')
elif my_set == ('YorM', 'Y'):
    print('MMYY')
elif my_set == ('Y', 'YorM'):
    print('YYMM')
else:
    print('NA')
