s = input()
t = input()
s_list = []
t_list = []
for i in s:
    s_list.append(i)
for i in t:
    t_list.append(i)
operation = [i for i in range(len(s_list)) if s_list[i] != t_list[i]]
print(len(operation))