A,B,C = map(int, input().split())
a = [A]
b = [B]
c = [C]
count = 0
sum = A + B + C
for i in range(10 ** 9):

    if a[i] == b[i] == c[i]:
        if a[i] % 2 == 0 and b[i] % 2 == 0 and c[i] % 2 == 0:
            count = -1
            break
        else:
            count = 0
            break
    elif a[i] % 2 == 0 and b[i] % 2 == 0 and c[i] % 2 == 0:
        a.append(b[i] / 2 + c[i] / 2)
        b.append(a[i] / 2 + c[i] / 2)
        c.append(a[i] / 2 + b[i] / 2)
        count += 1
    else:
        break


print(count)
