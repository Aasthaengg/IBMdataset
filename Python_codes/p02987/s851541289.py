s = input()
u = list(set(list(s)))
if len(u) == 2 and s.count(u[0]) == 2 and s.count(u[1]) == 2:
    print("Yes")
else:
    print("No")