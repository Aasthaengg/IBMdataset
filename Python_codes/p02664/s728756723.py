t = input()
n = len(t)
s_list = list(t)
for i in range(len(s_list)-1):
    if s_list[i] == '?':
        if s_list[i+1] == 'D' and s_list[i-1] == 'D':
            s_list[i] = 'P'
        elif s_list[i+1] == 'D' and s_list[i-1] == 'P':
            s_list[i] = 'D'
        elif s_list[i+1] == 'P' and s_list[i-1] == 'P':
            s_list[i] = 'D'
        elif s_list[i+1] == '?' and s_list[i-1] == 'D':
            s_list[i] = 'P'
        elif s_list[i+1] == '?' and s_list[i-1] == 'P':
            s_list[i] = 'D'
        else:
            s_list[i] = 'D'
if s_list[-1] == "?":
    s_list[-1] = 'D'


t = ''.join(s_list)
print(t)