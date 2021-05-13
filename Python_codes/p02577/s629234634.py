D = input()
dlist = [int(x) for x in D]
ans = 0

for i in range (0, len(dlist)):
    ans += dlist[i]

if ans % 9 == 0:
    print("Yes")
else:
    print("No")