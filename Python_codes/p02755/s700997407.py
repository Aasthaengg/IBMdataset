import sys
a, b = map(int,input().split())
lsta = []
lstb = []
if (a%2 == 1):
    lsta.append(int(a*12.5//1 + 1))
else:
    lsta.append(int(a*12.5))
for i in range(12):
    if ((lsta[0] + i + 1)*0.08//1 == a):
        lsta.append(lsta[0] + i + 1)

lstb.append(b*10)
for i in range(9):
    lstb.append(lstb[0] + i + 1)

for i in range(len(lsta)):
    if (lsta[i] in lstb):
        print(lsta[i])
        sys.exit()

print(-1)
        
