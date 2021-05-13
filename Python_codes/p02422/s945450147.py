str_in, n = input(), int(input())
for i in range(n):
    com = input().split()
    com_idx = [int(i) for i in com if i.isdigit()]
    if com[0]=="print":
        print(str_in[com_idx[0]:com_idx[1]+1])
    elif com[0]=="reverse":
        str_rev = str_in[com_idx[0]:com_idx[1]+1]
        str_in = str_in[:com_idx[0]] + str_rev[::-1] + str_in[com_idx[1]+1:]
    elif com[0]=="replace":
        str_in = str_in[:com_idx[0]] + com[3] + str_in[com_idx[1]+1:]

