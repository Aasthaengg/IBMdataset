n = int(input())
a = input()
b = input()
c = input()
res = 0
for i in range(n):
    x,y,z = a[i], b[i], c[i]
    if x==y==z:
        res += 0
    elif x==y or y==z or z==x:
        res += 1
    else:
        res += 2
print(res)