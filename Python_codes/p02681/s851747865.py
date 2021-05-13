s = input()
t = input()
check = len(s) + 1 == len(t) and s == t[:-1]
print("Yes" if check else "No")