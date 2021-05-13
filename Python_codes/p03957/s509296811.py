import sys

s = list(input())
cm = []
fM = []
for i, j in enumerate(s):
    if j == "C":
        cm.append(i)
    if j == "F":
        fM.append(i)
if "C" not in s or "F" not in s:
    print("No")
    sys.exit()
if max(fM) - min(cm) > 0:
    print("Yes")
else:
    print("No")