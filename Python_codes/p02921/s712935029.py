#!/usr/bin/env python3
print(sum(i == j for i, j in zip(*open(0).read().split())))
