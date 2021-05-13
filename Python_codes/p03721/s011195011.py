n,k = map(int,input().split())
dic = {}

for i in range(n):
    a,b = map(int,input().split())
    if a not in dic:
        dic[a] = b
    else:
        dic[a] += b

dic2 = sorted(dic.items())
c = 0
for i in dic2:
    c += i[1]
    if c >= k:
        print(i[0])
        exit()


