# -*- coding: utf-8 -*-

#----------
A,B,C,D = [int(input().strip()) for _ in range(4)]
#----------

ans = min(A,B)+min(C,D)
print(ans)
