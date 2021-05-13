i = input().split()

a,b,t = list(map(float, i))

c = 1
bisc = 0
na = a

while(na <= t):
    bisc = bisc + b
    c += 1
    na = a * c

print(int(bisc))
