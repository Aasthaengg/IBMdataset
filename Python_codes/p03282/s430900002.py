S = input()
k = int(input())

days = 5*10*15

for s in S:
    si = int(s)
    if si == 1:
        k -= 1
    else:
        k -= si**days

    if k <= 0:
        print(si)
        break
