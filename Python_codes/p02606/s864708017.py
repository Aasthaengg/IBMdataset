d: object
L,R, d = map(int, input().split())


num_list = list()

for x in range(L, R + 1):
    num_list.append(x)

dmul_list = list()
for i in num_list:
    x = i%d
    if x == 0:
        dmul_list.append(i)

print(len(dmul_list))