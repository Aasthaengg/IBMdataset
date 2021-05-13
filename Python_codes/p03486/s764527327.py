s = input()
t = input()

s_list = [c for c in s]
t_list = [c for c in t]

s_list.sort()
t_list.sort()

sd = "".join(s_list)
td = "".join(t_list[::-1])

if sd < td:
    print("Yes")
else:
    print("No")

