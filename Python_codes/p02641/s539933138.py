X,N,*P = map(int, open(0).read().split())

i = 0
while True:
    r = X - i 
    if r not in P:
        print(r)
        break
    l = X + i
    if l not in P:
        print(l)
        break
    i += 1