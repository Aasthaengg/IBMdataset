N = int(input())
mx = 3503
found = False
for i in range(1, mx):
    for j in range(1, mx):
        if i*j*4 % N != 0:
            continue
        den = ((i*j*4)//N) - i - j
        num = i*j
        if den == 0:
            continue
        if num%den == 0 and num//den > 0 and num//den < mx:
            print(i,j,num//den)
            found = True
            break
    if found:
        break