n = input()

if len(n) < 2:
    print(n)
    exit()

kumi = []
iti = 0

for x in range(2 ** (len(n) -1)):
    for m in range(len(n) -1):
        if (x >> m) & 1:
            kumi.append(n[iti:m+1])
            iti = m+1
        if m == len(n) -2:
            kumi.append(n[iti:m+2])
    iti = 0

kumi_int =[int(s) for s in kumi]
print(sum(kumi_int))