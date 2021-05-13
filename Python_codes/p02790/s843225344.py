import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

# N =I()
a,b= LI()
#AB = [LI() for _ in range(N)]
#A,B = zip(*AB)
#Ap = np.array(A)
#C = np.zeros(N + 1)

def generateStr(s,n):
    result = ''
    temp = str(s)
    for _ in range(n):
        result += temp 
    return result

a_str = generateStr(a,b)
b_str = generateStr(b, a)

if a_str<b_str:
    print(a_str)
else:
    print(b_str)