# -*- coding: utf-8 -*-
from itertools import combinations

print(min(map(lambda x: sum(x), list(combinations(list(map(int, input().split())), 2)))))
