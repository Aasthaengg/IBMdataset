a = input()
l = sorted(list(a))

if l[0] == l[1] and l[2] == l[3] and l[0] != l[2]:
    print("Yes")
else:
    print("No")