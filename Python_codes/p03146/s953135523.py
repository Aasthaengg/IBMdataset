s = int(input())
a = s
lis = list()

while True:
    if (s % 2) == 0:
        s = s / 2
        if s in lis:
            break
        lis.append(int(s))
    else:
        s = 3*s + 1
        if s in lis:
            break
        lis.append(int(s))
if (a ==1) or (a == 2) or (a == 4):
    print(4)
else:
    print(len(lis)+2)