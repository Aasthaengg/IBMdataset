NK = input().split()
Pn = input().split()
for i in range(int(NK[0])):
    Pn[i] = int(Pn[i])
Pn.sort()
s = 0
for i in range(int(NK[1])):
    s += Pn[i]
print(s)