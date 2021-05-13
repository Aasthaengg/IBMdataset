n = int(input())
l = [input().split() for i in range(n)]

s= 0

for i in range(n):
    if l[i][1] == 'JPY':
        s+=float(l[i][0])
    else:
        s+=float(l[i][0])*380000.0
print(s)