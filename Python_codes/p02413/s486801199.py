#coding:utf-8

r , c = [int(i) for i in input().rstrip().split()]
hyou =[]
r1=[]

#r????????§
for i in range(r):
    a = [int(i) for i in input().rstrip().split()]
    gou = sum(a)
    a.append(gou)
    print(" ".join(list(map(str ,a))))
    hyou.append(a)
    gou =0

#r+1
for i in range(c+1):
    for j in range(r):
       gou += hyou[j][i]


    r1.append(gou)
    gou = 0

#print(hyou)

print(" ".join(list(map(str ,r1))))