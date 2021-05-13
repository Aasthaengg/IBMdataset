s = int(input())
lst = [s]

for i in range(10**6):
    if int(lst[-1]) & 1 == 0:
        next_a = lst[-1]/2
        if next_a in lst:
            m = i + 1
            break
        lst.append(next_a)
    else:
        next_aa = 3*lst[-1] +1
        if next_aa in lst:
            m = i + 1
            break
        lst.append(next_aa)

print(m+1)