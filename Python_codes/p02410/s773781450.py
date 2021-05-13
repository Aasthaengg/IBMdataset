#coding:utf-8

n, m =[int(i) for i in input().rstrip().split(" ")]

a =[]
b =[]
#a
for i in range(n):
    d = [int(j) for j in input().rstrip().split(" ")]
    a.append(d)
#b
for i in range(m):
    b.append(int(input().rstrip()))

for i in range(n):
    ai = list(a[i])
    c = [j*k for j,k in zip(ai,b)]
    print(sum(c))