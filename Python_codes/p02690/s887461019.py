X = int(input()) 
flag = 0
for j in range(-120, 120):
    if flag == 1:
        break
    for k in range(j+1, 120):
        if k**5 - j**5 == X:
            print(k,j)
            flag = 1
            break
