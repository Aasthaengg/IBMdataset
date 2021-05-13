# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

T,X = list(map(int, input().rstrip().split()))
ans = T/X
print( Decimal(str(ans)).quantize(Decimal('0.0000000001'), rounding=ROUND_HALF_UP) )
