num = int(input())

table = []
for i in range(num):
    table.append(int(input()))

table2 = sorted(table, reverse=True)

for j in range(num):
    if table[j] != table2[0]:
        print(table2[0])
    else:
        print(table2[1])