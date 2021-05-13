n = int(input())
cnts = []
i = 0
while i*(i+1)//2 <= n:
    i += 1
    cnts.append(i)

rm = sum(cnts) - n
for i in cnts:
    if i == rm:continue
    print(i)