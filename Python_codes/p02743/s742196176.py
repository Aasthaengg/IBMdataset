a,b,c=map(int,input().split())

def ab_lt_c(a,b,c):
  d=c-a-b
  if d>0 and d*d > 4*a*b:
     return 'Yes'
  else:
     return 'No'

print(ab_lt_c(a,b,c))