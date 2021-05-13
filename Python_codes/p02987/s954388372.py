s = input()
a = [i for i in s]
a1 = list(set(a))

print("Yes" if len(a1) == a.count(a1[0]) == 2 else "No")