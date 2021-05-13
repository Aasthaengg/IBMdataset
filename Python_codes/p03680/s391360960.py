n = int(input())
a = []
for i in range(n):
    a1 = int(input())
    a.append(a1)
z = -1
s = 0
for h in range(n):
    if a[s] == 2:
        z = 'Yes'
        z = h+1
        break
    else:
        s = a[s]-1
print(z)