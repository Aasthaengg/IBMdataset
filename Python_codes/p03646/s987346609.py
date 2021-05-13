k = int(input())

b = k%50
c = k//50

a = [i+c for i in range(50)]

for i in range(b):
    a[-i-1] += 1

print(50)

for i in range(50):
    print(a[i],end=' ')
