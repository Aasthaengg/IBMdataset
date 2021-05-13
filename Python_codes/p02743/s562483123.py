a,b,c = map(int,input().split())
print('Yes' if c-a-b>0 and 4*a*b<c**2+a**2+b**2-2*a*c-2*b*c+2*a*b else 'No')
