s = list(input())
t = list(input())

s_ord = sorted(list(map(ord, s)))
t_ord = sorted(list(map(ord, t)), reverse=True)

for i in range(min([len(s_ord), len(t_ord)])):
    if t_ord[i] > s_ord[i]:
        print("Yes")
        break
else:
    if len(s_ord) < len(t_ord) and s_ord == t_ord[:len(s_ord)]:
        print("Yes")
    else:
        print("No")
