# -*- coding: utf-8 -*-

n = int(input())

l_a = sorted(map(int, input().split()), reverse=True)

print(sum([((-1)**(i%2))*a for i, a in enumerate(l_a)]))
