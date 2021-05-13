packs = input().split()
p_list = []

for i in packs:
    p_list.append(int(i))


list.sort(p_list)

if p_list[0]+p_list[1] == p_list[2]:
    print('Yes')
else:
    print('No')
