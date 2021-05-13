n,m = map(int,input().split())
a = 1900*m+100*(n-m)
b = 1-(1/2)**m
print(int(1900*m+100*(n-m)+(a*b)/(1-b)))