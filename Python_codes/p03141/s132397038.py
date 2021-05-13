import copy
n = int(input())
dish = []
for i in range(n):
    a,b = map(int,input().split())
    dish.append((a,b, a+b))
dish.sort(key=lambda x:x[2])
dish.reverse()
tk = dish[0:n:2]
ao = dish[1:n:2]
tkp = 0
aop = 0
for i in range(len(tk)):
    tkp += tk[i][0]
for i in range(len(ao)):
    aop += ao[i][1]
print(tkp-aop)




