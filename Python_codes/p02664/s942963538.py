T = input()
T_list = list(T)
i = 0
while i < len(T):
    if T_list[i] == "?":
        T_list[i] = "D"
    i += 1
T_new = "".join(T_list)
print(T_new)