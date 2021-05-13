S = input()
s_list = [s for s in S]
s_set = set(s_list)
if len(s_list)==len(s_set):
    print('yes')
else:
    print('no')