#!/usr/bin/python

input_data = list(map(int,input().split()))

d1 = input_data[0]
d2 = input_data[1]
d3 = input_data[2]

d4 = int(d2 / d1)
if d4 > d3:
    total = d3
else:
    total = d4

print(total)

