n,a,b=map(int,input().split())
bet=abs(b-a)
if bet%2==0:
  winner='Alice'
else:
    winner='Borys'
    
print(winner)