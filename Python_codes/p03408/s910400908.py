n = int(input())


dic_blue = {}
for i in range(n):
    a = str(input())
    if a in dic_blue:
        dic_blue[a] += 1
    else:
        dic_blue[a] = 1

m = int(input())
dic_red = {}
for i in range(m):
    b = str(input())
    if b in dic_red:
        dic_red[b] += 1
    else:
        dic_red[b] = 1

total_list = []
total_list.append(0)
for j in dic_blue.keys():
    total = 0
    if j in dic_red:
        total = dic_blue[j] - dic_red[j]
        total_list.append(total)
    else:
        total = dic_blue[j]
        total_list.append(total)

print(max(total_list))