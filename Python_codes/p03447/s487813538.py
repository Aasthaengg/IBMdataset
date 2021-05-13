# -*- coding: utf-8 -*-

#----------
X,A,B = [int(input().strip()) for _ in range(3)]
#----------
num_B = (X-A) // B
ans = X - (A + num_B * B)

print(ans)
