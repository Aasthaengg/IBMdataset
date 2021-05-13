dish = [int(input()) for i in range(5)]
s = sum(dish)
l = []
l_d =[]

for i in range(5):
    if dish[i]%10 != 0:
        l.append(dish[i]%10)

for i in l:
    l_d.append(-(i-10))

print(s+sum(sorted(l_d)[:-1]))