s = int(input())

used = set([s])
a = s
for i in range(2, 1000000):
    if a % 2 == 0:
        next = a // 2
    else:
        next = 3 * a + 1

    if next in used:
        print(i)
        break
    else:
        used.add(next)
        a = next
