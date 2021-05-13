import string

while True:
    L = string.split(raw_input())
    x = int(L[0])
    y = int(L[1])
    if x == 0 and y == 0: break
    
    if x < y:
        print x,y
    else:
        print y,x