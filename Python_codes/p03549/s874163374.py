from decimal import Decimal, ROUND_HALF_UP
n,m=map(int,input().split())
X=((n-m)*100+1900*m)*(0.5**m)
j=0
for i in range(10**6):
    j+=X*i*((1-(0.5)**m)**(i-1))

print(Decimal(str(j)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))