line = int(input())

s_set = [x for x in range(1, 14)]
h_set = s_set[:]
c_set = s_set[:]
d_set = s_set[:]

taro_list = []
for i in range(line):
    taro_list.append(input())

for card in taro_list:
    suite = card.split(" ")[0]
    num = int(card.split(" ")[1])
    if suite == "S": s_set.remove(num)
    if suite == "H": h_set.remove(num)
    if suite == "C": c_set.remove(num)
    if suite == "D": d_set.remove(num)

for e in s_set:
    print("S " + str(e))

for e in h_set:
    print("H " + str(e))


for e in c_set:
    print("C " + str(e))

for e in d_set:
    print("D " + str(e))