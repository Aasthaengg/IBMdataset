e = input()
f = input()
g = input()
h = input()

a = int(e)
b = int(f)
c = int(g)
x = int(h)

answer = 0

arrays = []
for i in range(125001):
    arrays.append(0)

for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            arrays[500 * i + 100 * j + 50 * k] += 1

answer = arrays[x]
print(answer)