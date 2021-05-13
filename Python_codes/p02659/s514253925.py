from sys import stdin
import sys

a, b = [x for x in stdin.readline().rstrip().split()]
a = int(a)
b = int(b.replace('.',''))

print(a * b  // 100)