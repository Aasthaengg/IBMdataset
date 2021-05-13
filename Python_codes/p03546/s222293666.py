#! env/bin/local python3
# -*- coding: utf-8 -*-

import numpy as np

inputs = []

while True:
    try:
        inputs.append([int(i) for i in input().split()])
    except EOFError:
        break

h, w = inputs[0]
c = inputs[1: 11]
a = inputs[11:]

number_of_edge = 10
number_of_node = 10

for k in range(number_of_node):
    for i in range(number_of_node):
        for j in range(number_of_node):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

target = []
for ca in a:
    target += ca

target = [ta for ta in target if np.abs(ta) != 1]
results = 0
for t in target:
    results += c[t][1]

print(results)

