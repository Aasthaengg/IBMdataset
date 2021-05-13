# -*- coding: utf-8 -*-
N = list(input())
print(['No', 'Yes'][N[1] == N[2] and (N[0] == N[1] or N[2] == N[3])])