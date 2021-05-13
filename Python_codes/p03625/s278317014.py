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
h = 0
w = 0
while i < len(dic2):
    if dic2[i][1] >= 4 and h == 0 and w == 0:
        print(dic2[i][0]**2)
        exit()
    if dic2[i][1] >= 2 and h == 0:
        h = dic2[i][0]
    elif dic2[i][1] >= 2 and h != 0:
        print(h*dic2[i][0])
        exit()
    i += 1

print(0)