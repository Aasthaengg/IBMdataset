n = str(input())
if len(n) <= 2:
    print(0)
else:
    a = n[0:-2]
    tens = int(n[-2])
    need = tens*2
    ones = int(n[-1])
    if ones == 0:
        need +=0
    elif ones <= 5:
        need += 1
    else:
        need +=2
    if need <= int(a):
        print(1)
    else:
        print(0)
