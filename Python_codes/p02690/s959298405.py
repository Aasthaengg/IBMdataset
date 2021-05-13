x = int(input())
Pow = [1]
curr = 2
while True:
    if curr**5 - Pow[-1]**5 > x:
        break
    Pow.append(curr)
    curr += 1

mx = Pow[-1]
for i in range(mx + 1):
    Pow.append(-i)

for i in Pow:
    for j in Pow:
        if i**5 - j**5 == x:
            print(i, j)
            exit(0)

