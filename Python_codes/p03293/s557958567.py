S = input()
T = input()
S_len = len(S)

s = S
for i in range(S_len):
    s_list = list(s)
    s_end = s_list.pop()
    b = s_end + ''.join(s_list)
    if b == T:
        print('Yes')
        exit(0)
    s = b
print('No')

