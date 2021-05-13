n = int(input())
s = list(map(int,input().split()))

dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

dic2 = sorted(dic.items(),reverse=True)#[(4, 1), (3, 1), (2, 2), (1, 2)]

i = 0
tmp = 0
sq = 0
while i < len(dic2):
    if dic2[i][1] >= 4 and sq == 0:
        sq = (dic2[i][0])**2
    if dic2[i][1] >= 2 and tmp == 0:
        tmp = dic2[i][0]
    elif dic2[i][1] >= 2 and tmp != 0:
        print(max(sq,tmp*dic2[i][0]))
        exit()
    i += 1

if sq == 0:
    print(0)
else:
    print(sq)