# -*- coding: utf-8 -*-
n,k = list(map(int,input().split()))
ret = k * (k-1)**(n-1)
print(ret)