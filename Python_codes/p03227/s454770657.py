S = input()
if len(S) == 3:
    S_list = list(S)
    S_list.reverse()
    print("".join(S_list))
else:
    print(S)