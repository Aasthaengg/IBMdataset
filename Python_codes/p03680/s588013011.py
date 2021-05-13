n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
#print(a)
tmp = 1
isOK = -1
for i in range(1,n+1):
    if a[tmp]==2:
        isOK = i
        break
    tmp = a[tmp]

print(isOK)