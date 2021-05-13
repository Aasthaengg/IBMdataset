n = int(input())
a = []
b = 0
i = 1
while b < n:
    a.append(i)
    b += i
    i += 1
b -= n
for i in a:
    if i != b:
        print(i)