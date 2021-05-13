s = input()
x,y = map(int,input().split())

XY = [[],[]]
i = 0
xy = 0
for c in s+"T":
    if c == "T":
        XY[xy].append(i)
        i = 0
        xy = 1-xy
    else:
        i+=1

xset = set((XY[0][0],))
yset = set((0,))
for X in XY[0][1:]:
    xset = set(i + X for i in xset) | set(i - X for i in xset)
for Y in XY[1]:
    yset = set(i + Y for i in yset) | set(i - Y for i in yset)
if x in xset and y in yset:
    print("Yes")
else:
    print("No")