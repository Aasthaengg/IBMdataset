s = list(str(input()))
d = dict.fromkeys(s)
if len(s) == len(d):
    print('yes')
else:
    print('no')