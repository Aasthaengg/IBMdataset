s = input()
t = input()

# print(s)
# print(t)

s_list = list(s)
t_list = list(t)
# print(s_list)
# print(t_list)    

s_list_sorted = sorted(s_list)
t_list_sorted = sorted(t_list, reverse=True)
# print(s_list_sorted)
# print(t_list_sorted)

s_sorted = ''.join(s_list_sorted)
t_sorted = ''.join(t_list_sorted)
# print(s_sorted)
# print(t_sorted)

if s_sorted < t_sorted:
    print("Yes")
else:
    print("No")