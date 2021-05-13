input()
a = [int(x) for x in input().split()]
a = [x - 1 for x in a]
c = 0
for i in range(len(a)):
    if(i % 2 == 0 and a[i] % 2 == 0):
        c += 1
print(c)        