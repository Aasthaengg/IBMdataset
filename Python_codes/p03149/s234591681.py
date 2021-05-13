import itertools
t = False
num = [s for s in input().split()]
lister = list(itertools.permutations(num))
for i in range(24):
    s = lister[i]
    if s[0] == "1" and s[1] == "9" and s[2] == "7" and s[3] == "4":
        t = True
if t == True:
    print("YES")
else:
    print("NO")