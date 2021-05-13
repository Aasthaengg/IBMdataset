N = int(input())
N2 = str(N)
a = list(N2)
s = 0
for i in a:
    s += int(i)
if s%9 == 0:
    print("Yes")
else:
    print("No")