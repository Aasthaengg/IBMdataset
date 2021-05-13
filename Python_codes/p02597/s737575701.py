N = int(input())
C = input()
c = []
for i in C:
    c.append(i)

a = c.count("R")

count = 0
for b in c[0:a]:
    if b == "R":
        count += 1


print(a - count)