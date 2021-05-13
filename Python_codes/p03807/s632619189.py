# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))

print('YES' if len([i for i in a if i%2==1])%2==0 else 'NO')