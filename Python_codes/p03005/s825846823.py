from sys import stdin
import string

n,k = [int(x) for x in stdin.readline().rstrip().split()]

if k == 1:
    print(0)
    exit()
print(n-k)