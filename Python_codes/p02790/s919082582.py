# n,m = map(int,input().split())
a,b = map(int,input().split())

m = a * str(b)
n = b * str(a)

list = []
list.append(m)
list.append(n)

list.sort()
print(list[0])