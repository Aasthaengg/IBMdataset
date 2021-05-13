#!/usr/bin/env python3
(h, w), *p = [i.split() for i in open(0)]
h = int(h)
w = int(w)+2
print("#" * w)
for i in p:
    print("#{}#".format(*i))
print("#" * w)
