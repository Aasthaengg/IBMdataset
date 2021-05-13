n = int(input())
s = input()
Rcount = 0
Bcount = 0
for i in range(n):
    if s[i] == "R":
        Rcount += 1
    else:
        Bcount += 1
if Rcount > Bcount:
    print("Yes")
else:
    print("No")