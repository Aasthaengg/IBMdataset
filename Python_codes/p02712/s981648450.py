n = int(input())

a = n // 15
c = a*(a-1)//2
b = n % 15

l = [1, 2, 0, 4, 0, 0, 7, 8, 0, 0, 11, 0, 13, 14]
for i in range(len(l)):
    if l[i] != 0:
        l[i] += 15*a

print(60*a + 120*c + sum(l[:b]) )