n = int(input())
a,b = map(str,input().split())
c =[]
for i in range(n):
    c.append(a[i])
    c.append(b[i])
c1 = "".join(c)
print(c1)