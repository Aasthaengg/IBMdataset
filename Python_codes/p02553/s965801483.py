'''
Problem Link - https://atcoder.jp/contests/abc178/tasks/abc178_b
'''
from sys import stdin,stdout
from math import *
from collections import *

mod = 1000000007

def gcd(a,b):
	while b:
		a,b = b,a%b
	return a

def lcm(a,b): return (a*b) // gcd(a,b)

def set_bits(X):
	c = 0
	while X:
		X &= (X-1);c += 1
	return c

def compute_MOD(N,M): return (N%M + M) % M

def get_array(): return list(map(int, stdin.readline().split()))
 
def get_ints(): return map(int, stdin.readline().split())

def get_int(): return int(stdin.readline())

def get_input(): return stdin.readline().strip()

def main():
	a,b,c,d = get_ints()
	stdout.write(str(max(a*c,a*d,b*c,b*d))+'\n')

if __name__ == "__main__":
    main()