n = int(input())
list = []
for i in range(n):
    list.append(input())
for s in ["S", "H", "C", "D"]:
    for r in range(1, 14):
        if s + " " + str(r) not in list:
            print(s,r)