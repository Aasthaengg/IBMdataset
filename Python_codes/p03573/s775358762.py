# -*- coding: utf-8 -*-


#----------
A,B,C = list(map(int, input().rstrip().split()))
#----------

print( A if B==C else B if A==C else C if A==B else "" )
