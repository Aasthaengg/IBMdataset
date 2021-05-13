s = set(input())
a = set("abcdefghijklmnopqrstuvwxyz")
d = a - s
if d:
    print(sorted(d)[0])
else:
    print("None")