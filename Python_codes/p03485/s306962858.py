# -*- coding: utf-8 -*-
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


nums = list(map(int, input().rstrip().split()))

#----------
average = (nums[0] + nums[1]) / 2
print( Decimal(str(average)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
