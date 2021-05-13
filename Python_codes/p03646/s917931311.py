k=int(input());n=50;print(n);print(*[n+k//n if i<k%n else n+(k//n-1)-k%n for i in range(n)])
