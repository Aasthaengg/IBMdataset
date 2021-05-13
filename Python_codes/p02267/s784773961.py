#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
stdin.readline()
s = {int(s) for s in stdin.readline().split()}
stdin.readline()
s.intersection_update((int(s) for s in stdin.readline().split()))
print(len(s))