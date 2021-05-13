n,m,d = [int(x) for x in input().split()]

dif= ((n-d)*min(2,d+1) )/  (n**2)

print(dif*(m-1))