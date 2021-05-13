N = int(input())
mass = []

for i in range(N):
    a,b = input().split()
    a = float(a)
    if b == "BTC":
        a *= 380000.0
    mass.append(a)

print(sum(mass))
