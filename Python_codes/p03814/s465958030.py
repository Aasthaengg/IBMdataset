s = list(input())
a = int(s.index("A"))
del s[:a]

list_z = [i for i, x in enumerate(s) if x =="Z"]
z = max(list_z)
del s[len(s):z:-1]
print(len(s))
