s = list(map(str, input()))
s2 = list(set(s))
if len(s) == len(s2):
    print("yes")
else:
    print("no")