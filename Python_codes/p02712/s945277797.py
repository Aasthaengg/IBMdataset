n=int(input())
l3 = (n//3)*3
l5= (n//5)*5
l15=(n//15)*15
print(n*(n+1)//2 - (3+l3)*l3//6 - (5+l5)*l5//10 + (15+l15)*l15//30  )