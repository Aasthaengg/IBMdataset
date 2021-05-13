#x = [int(x) for x in input().split()]
x = int(input())
y = int(input())
z = [1,2,3]
del(z[z.index(x)])
del(z[z.index(y)])
print(z[0])
