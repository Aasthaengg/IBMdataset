# -*- coding: utf-8 -*-
import sys
import math
from decimal import Decimal, ROUND_HALF_UP


def main():
    N,K = list(map(int, sys.stdin.readline().split()))
    A_list = list(map(int, sys.stdin.readline().split()))
 
 
    def check(length :int) -> bool:
        cnt = 0
 
        for a in A_list:
            if a >= length:
                divide = math.ceil(a / length)
                cnt += (divide - 1)
        
        return (True if cnt <= K else False)
 
 
    L = 0.1          # the minimum length
    R = max(A_list)  # the maximum length
 
    while (R - L) > 0.01:
        M = L + (R - L) / 2
 
        if check(M):
            R = M
        else:
            L = M
    
    
    ans = Decimal(str(M)).quantize(Decimal('1E-1'), rounding=ROUND_HALF_UP)
    ans = math.ceil(ans)

    print(ans)



if __name__ == "__main__":
    main()
