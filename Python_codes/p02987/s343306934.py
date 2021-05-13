s = input()
dic = {}
for x in s:
    if(dic.get(x) is None):
        dic[x] = 1
    else:
        dic[x] += 1

for i in dic.values():
    if(i!=2):
        print('No')
        exit()

print('Yes')
