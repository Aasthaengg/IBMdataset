n = int(input())
al = list(int(input()) for _ in range(n))

al_s = sorted(al)
fir = al_s[-1]
sec = al_s[-2]

for a in al:
    if a == fir:
        print(sec)
    else:
        print(fir)
