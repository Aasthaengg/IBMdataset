n = list(map(int, input().split()))
sw = []
for x in range(n[1]):
    sw.append(list(map(int, input().split())))
p = list(map(int, input().split()))
kumi = 0

for a in range(2 **n[0]):
    akari = 0
    kai = []
    for b in range(n[0]):
        if ((a >> b)& 1):
            kai.append(b+1)
    #print(kai)
    for c in range(n[1]):
        hantei = 0
        for d in range(1,sw[c][0]+1):
            if kai.count(sw[c][d]) >= 1:
                hantei +=1
        if p[c] == 0 and hantei %2 ==0:
            akari += 1
        elif p[c] == 1 and hantei %2 !=0:
            akari += 1
    if akari == n[1]:
        kumi += 1

print(kumi)