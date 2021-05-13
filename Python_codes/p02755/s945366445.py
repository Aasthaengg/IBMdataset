a,b = map(int,input().split())

taxfree = 1

while True:
    if int(taxfree*0.08)==a and int(taxfree*0.1)==b:
        break
    taxfree += 1
    if taxfree == 1001:
        taxfree = -1
        break

print(taxfree)
