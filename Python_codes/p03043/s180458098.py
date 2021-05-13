n,k = map(int,input().split())
chance = 0
for i in range(1,1+n):
    dini = i
    j = 0
    while dini < k:
        dini *= 2
        j += 1
    chance += 0.5**j
print(chance/n)