s = int(input())
a = [s]

while True:
    i = int(a[-1]/2) if a[-1] % 2 == 0 else a[-1]*3+1
    if i in a:
        print(len(a)+1)
        break
    else:
        a.append(i)

