S = input()

if len(S)==2:
    print(S)
else:
    S_list = [list for list in S]
    S_list.reverse()
    print(''.join(S_list))