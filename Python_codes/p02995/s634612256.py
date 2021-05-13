import math
A,B,C,D = map(int,input().split())
BIkaCbaisuC = B//C
AIkaCbaisuC = (A-1)//C
ABkanCbaisuC = BIkaCbaisuC - AIkaCbaisuC

BIkaDbaisuC = B//D
AIkaDbaisuC = (A-1)//D
ABkanDbaisuC = BIkaDbaisuC - AIkaDbaisuC

cd = math.floor(C*D/math.gcd(C,D))
BIkacdbaisuC = B//cd
AIkacdbaisuC = (A-1)//cd
ABkancdbaisuC = BIkacdbaisuC - AIkacdbaisuC

print(B-A+1-ABkanCbaisuC-ABkanDbaisuC+ABkancdbaisuC)
