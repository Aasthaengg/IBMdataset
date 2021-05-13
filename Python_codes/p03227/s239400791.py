S = input()

if len(S) == 2:
    print(S)
elif len(S) == 3:
    #str_list = list(reversed(S))
    new_str = ''.join(list(reversed(S)))
    print(new_str)