n = int(input())
dic = {}
for i in range(n):
    a = int(input())
    dic.setdefault(a,0)
    dic[a] += 1
    if dic[a] == 2:
        dic.pop(a)

print(len(dic))