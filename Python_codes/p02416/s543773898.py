array = []
while True:
    n = int(input())
    if n != 0:
        array.append(n)
    else:
        break
for i in range(len(array)):
    data = str(array[i])
    s = 0
    for c in data:
        s += int(c)
    print(s)