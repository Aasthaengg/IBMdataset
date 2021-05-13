S_list = list(input())

for i in range(0, len(S_list), 2):
    if S_list[i] == 'R' or S_list[i] == 'U' or S_list[i] == 'D':
        pass
    else:
        print('No')
        exit()

for i in range(1, len(S_list), 2):
    if S_list[i] == 'L' or S_list[i] == 'U' or S_list[i] == 'D':
        pass
    else:
        print('No')
        exit()

print('Yes')
