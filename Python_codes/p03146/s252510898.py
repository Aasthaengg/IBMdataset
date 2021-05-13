s = int(input())
a = [s]
for i in range(1000000):
    if a[i] % 2:
        a.append(3 * a[i] + 1)
    else:
        a.append(a[i] // 2)

    if len(set(a)) != len(a):
        print(i + 2)
        break
