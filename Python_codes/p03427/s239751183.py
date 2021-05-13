n=int(input())
k=len(str(n))
c=n//10**(k-1)
print(c+9*(k-1) if n==(c+1)*10**(k-1)-1 else c+9*(k-1)-1)
