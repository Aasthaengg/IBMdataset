s = input()

n = list(s)

sets = set(n)

if len(n) == len(sets):
    print("yes")
else:
    print("no")