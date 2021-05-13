# -*- coding: utf-8 -*-
N, A = map(int, open(0))
print(['No', 'Yes'][N % 500 <= A])