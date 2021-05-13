n = int(input())

i = 1
while True:
    t = i*i
    if t == n:
        print(t)
        exit()
    elif t > n:
        print((i-1)*(i-1))
        exit()
    
    i += 1