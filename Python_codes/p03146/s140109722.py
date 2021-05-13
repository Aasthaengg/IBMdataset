s = int(input())

a = [s]
ai = s
for i in range(2, 10**6 + 2):
    if ai % 2 == 0:
        ai = ai/2
        if ai in a:
            print(i)
            break
    else:
        ai = 3*ai + 1
        if ai in a:
            print(i)
            break
    a.append(ai)