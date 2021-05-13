import math
k = int(input());
    
sum = 0;
sum += (k*k*k-(k-1)*(k-1)*(k-1))

for p in range(2,k+1):
    for q in range(2,k+1):
        g = math.gcd(p,q);
        if g == 1:
            sum += k-1
        else:
            for r in range(2,k+1):
                sum += math.gcd(g,r);
            
print(sum);