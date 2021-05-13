s = input()
s_list = []
for i in s:
    s_list.append(i)
s_list.sort()
if len(set(s_list)) == 2 and s_list[0] == s_list[1] and s_list[2] == s_list[3]:
    print("Yes")
else:
    print("No")