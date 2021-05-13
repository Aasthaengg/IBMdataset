n, s = open(0)
a=['']
for i in s.split():
    a.insert(int(i)-1, i)
if a[-1] == "":
    print(*a)
else:
    print(-1)