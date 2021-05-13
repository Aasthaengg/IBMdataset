s = input()
p = input()
s_len = len(s)
p_len = len(p)
for i in range(s_len):
    for j in range(p_len):
        same = True
        if s[(i+j)%s_len] != p[j]:
            same = False
            break
    if same:
        print("Yes")
        exit(0)
print("No")

