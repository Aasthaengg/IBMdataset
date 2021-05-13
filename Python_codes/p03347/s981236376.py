n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if a[0] != 0:
    print("-1")
else:
    x = [0] * len(a)
    d = [0] * len(a)
    dd = [0] * len(a)

    c = 0
    s = 10**6
    #0 1 1 0 1 2 2 2 3
    wala = False
    for i in range(len(a) - 1, 0, -1):
        #print("-")
        if i <= s and a[i] == 0:
            #print("X")
            continue
        if i - a[i] < 0 or i - a[i] > s:
            #print("Y")
            wala = True
            break
        if s + a[i] == i:
            continue
        s = min(s, i - a[i])
        c += a[i]
    if wala:
        print("-1")
    else:
        print(c)
