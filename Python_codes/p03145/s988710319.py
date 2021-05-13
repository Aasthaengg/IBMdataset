k = input().split()
a = k[0]
b = k[1]
c = k[2]
for i in range(len(k)):
    k[i] = int(k[i])
h = max(k)

Buf = 1
del k[k.index(h)]

for i in k:
    Buf = Buf * int(i)
r = Buf/2
print(int(r))