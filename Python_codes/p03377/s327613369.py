# -*- coding: utf-8 -*-
A, B, X = map(int, input().split())
print(['NO', 'YES'][A <= X and (A + B) >= X])