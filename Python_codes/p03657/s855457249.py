a,b = map(int,input().split())
print(['P','Imp'][all([a%3>0,b%3>0,(a+b)%3>0])]+'ossible')