N = int(input())
for a in range(1,3501):
    for b in range(a,3501):
        m =  (4*a*b) - N*(a+b)
        if m> 0 and N*a*b % m == 0:
            c = (N*a*b)//m
            break
    else:
        continue
    break
print(a,b,c)
