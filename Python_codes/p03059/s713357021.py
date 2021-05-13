from operator import itemgetter
import sys
sys.setrecursionlimit(1000000)


a,b,t=map(int,input().split())

print((t//a)*b)
