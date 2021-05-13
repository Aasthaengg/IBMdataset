# -*- coding: utf-8 -*-

n, a, b = map(int, open(0).read().split())

print(sum([i for i in range(n+1) if a <= sum(list(map(int,list(str(i))))) <= b ]))
