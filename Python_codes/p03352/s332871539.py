X=int(input())
s=set(pow(i,j) for i in range(40) for j in range(2,10) if pow(i,j)<=X)
print(max(s))