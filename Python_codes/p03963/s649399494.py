# -*- coding: utf-8 -*-

#----------
N,K = list(map(int, input().rstrip().split()))
#----------
ans = K * (K-1)**(N-1)
print(ans)
