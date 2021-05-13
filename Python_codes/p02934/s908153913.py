# -*- coding: utf-8 -*-

n = int(input())
l_a = list(map(int, input().split()))

print(1/sum([1/a for a in l_a]))
