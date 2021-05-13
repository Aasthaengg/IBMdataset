a,b = map(int,input().split())
hachi = []
ju = []
kane = -1

for i in range(1250):
    if (i*8)//100 == a:
        hachi.append(i)
    if i//10 == b:
        ju.append(i)

for j in range(1250):
    if (1250-j in hachi)and(1250-j in ju):
        kane = 1250-j

print(kane)