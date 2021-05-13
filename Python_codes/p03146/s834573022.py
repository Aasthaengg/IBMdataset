l = [int(input())]

for i in range(1000000):
    a = l[-1] // 2 if l[-1] % 2 == 0 else l[-1] * 3 + 1
    if a in l:
        print(i + 2)
        break
    l.append(a)