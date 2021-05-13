a = int(input())

res = ''

i = 1
while True:
    x = i
    if x % 3 == 0:
        res += " " + str(i)
    else:
        while True:
            if x % 10 == 3:
                res += " " + str(i)
                break
            x = x // 10
            if x == 0:
                break
    i += 1
    if i > a:
        break

print(res)

