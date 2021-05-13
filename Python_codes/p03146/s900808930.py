s = int(input())
lst = [s]

cnt = 1
while True:
    if int(lst[-1]) & 1 == 0:
        cnt += 1
        next_a = lst[-1]/2
        if next_a in lst:
            m = cnt
            break
        lst.append(next_a)
        
    else:
        cnt += 1
        next_aa = 3*lst[-1] +1
        if next_aa in lst:
            m = cnt
            break
        lst.append(next_aa)

print(m)