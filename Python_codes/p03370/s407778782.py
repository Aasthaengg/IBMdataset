s = input().split()
n = int(s[0])
x = int(s[1])

donuts = []


for i in range(n):
    p = input()
    q = int(p)
    donuts.append(q)

donuts.sort()

min_donuts = donuts[0]
answer = len(donuts)

price = 0
for i in range(len(donuts)):
    price += donuts[i]

y = x - price
count = int(y / min_donuts)
answer += count
print(answer)

