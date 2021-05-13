# -*- coding: utf-8 -*-
total = sum(list(map(int, input().split())))

print(['error',total][total < 10])