a,b = map(int, input().split())

tasu = a +b
hiku = a - b
kake = a * b

line = [tasu,hiku,kake]
line.sort()

print(line[2])

