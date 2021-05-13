# -*- coding: utf-8 -*-
X, A, B = map(int, input().split())

state = "safe"
if A >= B:
    state = "delicious"
elif A+X < B:
    state = "dangerous"
    
print(state)