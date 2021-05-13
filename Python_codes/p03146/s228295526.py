n=int(input());a=[]
while n not in a: a.append(n);n=[3*n+1,n//2][n%2==0]
print(len(a)+1)