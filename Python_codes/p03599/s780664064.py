A,B,C,D,E,F = map(int,input().split())

max_w = 0
max_s = 0
dens = 0
for a in range((F//(100*A))+1):
    for b in range((F//(100*B))+1):
        for c in range((F//C)+1):
            for d in range((F//D)+1):
                if 100*(A*a+B*b) + c*C + d*D > F:
                    break
                elif (c*C+d*D) <= (A*a+B*b)*E and 100*(A*a+B*b) != 0:
                    temp_dens = (C*c+D*d)/(C*c+D*d+100*(A*a+B*b))
                    if temp_dens >= dens:
                        max_w = 100*(A*a+B*b)
                        max_s = C*c + D*d
                        dens = temp_dens
                    
print(max_w + max_s, max_s)