S = input()
len_S = len(S)

len_set_S = len(set(S))

if len_S == len_set_S:
    print('yes')
else:
    print('no')