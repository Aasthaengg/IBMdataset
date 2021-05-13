import sys,math,collections,itertools
input = sys.stdin.readline

N,M = list(map(int,input().split()))
ini_cost = M*1900+(N-M)*100
print(ini_cost*2**M)