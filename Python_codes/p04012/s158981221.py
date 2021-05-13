w = input()
dic = {}
for i in range(len(w)):
    if w[i] not in dic.keys():
        dic[w[i]] = 1
    else:
        dic[w[i]] += 1
flag = True
for i in dic.keys():
    if dic[i]%2 != 0:
        flag = False
if flag:
    print("Yes")
else:
    print("No")