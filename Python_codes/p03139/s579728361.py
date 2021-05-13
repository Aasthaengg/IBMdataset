from sys import stdin
import fractions

n,a,b = [int(x) for x in stdin.readline().rstrip().split()]

print(min(a,b),max(0,a+b-n))