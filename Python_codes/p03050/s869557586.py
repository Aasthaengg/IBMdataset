n = int(input())
factors = []
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        if n//i*2<(4*n+1)**0.5-1:
            factors.append(i)
        if i*2<(4*n+1)**0.5-1:
            factors.append(n//i)
print(sum(factors)-len(factors))