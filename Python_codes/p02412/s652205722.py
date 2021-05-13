# -*- coding: utf-8 -*-
while True:
    count=0
    n,x = [int(a)for a in input().split(' ')]
    if n+x==0:
        break
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if i + j + k ==x:
                    count += 1
    print(count)