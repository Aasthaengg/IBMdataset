X=int(input())
s=set(i**j for i in range(40) for j in range(2,10) if i**j<=X)
print(max(s))