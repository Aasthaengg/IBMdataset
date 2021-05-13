from sys import stdin
import collections

n,i = [int(x) for x in stdin.readline().rstrip().split()]

print(n-i+1)
