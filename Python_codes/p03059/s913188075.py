a,b,t = input().split()
a = int(a)
b = int(b)
t = int(t)
qtd = 0

if 1 <= a <= 20 :
    if 1 <= b <= 20:
        if 1 <= t <= 20:
            intera = a
            while intera <= t:
                qtd = qtd + b
                intera = intera + a
            print(qtd)