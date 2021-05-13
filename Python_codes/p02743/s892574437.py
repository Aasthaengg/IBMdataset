import numpy as np
import decimal

a,b,c = map(int,input().split())

if np.sqrt(decimal.Decimal(a)) +  np.sqrt(decimal.Decimal(b)) <  np.sqrt(decimal.Decimal(c)):
  print('Yes')

else:
  print('No')
