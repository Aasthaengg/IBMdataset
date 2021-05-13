n = int(input())
dic = {}
for i in range(n):
    d = int(input())
    dic.setdefault(d,0)
    dic[d] += 1
print(len(dic))