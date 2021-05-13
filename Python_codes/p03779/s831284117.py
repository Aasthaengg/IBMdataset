n=int(input())
p=int(-0.5+(2*n+0.25)**0.5)
q=p*(p+1)//2
print(p if q==n else p+1)