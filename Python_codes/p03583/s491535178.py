N = int(input())
for a in range(1,3501):
    for b in range(1,3501):
        if (4*a*b) - N*(a+b) != 0:
            r = (N*a*b) % ( (4*a*b) - N*(a+b) )
            if r == 0:
                c = (N*a*b) // ( (4*a*b) - N*(a+b) )
                if c > 0:
                    break
    else:
        continue
    break
print(a,b,c)