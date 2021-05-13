a, b, c = [int(x) for x in raw_input().split(" ")]
list =[a,b,c]
list_2 = []

for x in range(len(list)):
    mini = min(list)
    list_2.append(mini)
    list.remove(mini)

for x in range(0, len(list_2)):
    a = list_2[x]

    if x == 0:
        req = str(a) + " "
    else:
        req += str(a) + " "

q = req.rstrip()
print(q)