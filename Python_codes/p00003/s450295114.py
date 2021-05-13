# coding: utf-8
# Here your code !

n = int(input())
e = [[int(i) for i in input().split()] for i in range(n)] 
for i in e:
    a = max(i)
    i.remove(a)
    if a*a == i[0]*i[0]+ i[1]*i[1]:
        print("YES")
    else:
        print("NO")