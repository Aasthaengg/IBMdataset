#                               #
    # author : samars_diary #
    # 18-09-2020 │ 15:02:48 #
#                               #

import sys, os.path

#if(os.path.exists('input.txt')):
    #sys.stdin = open('input.txt',"r")
    #sys.stdout = open('output.txt',"w")

sys.setrecursionlimit(10 ** 5)

def mod(): return 10**9+7
def i(): return sys.stdin.readline().strip()
def ii(): return int(sys.stdin.readline())
def li(): return list(sys.stdin.readline().strip())
def mii(): return map(int, sys.stdin.readline().split())
def lii(): return list(map(int, sys.stdin.readline().strip().split()))

#print=sys.stdout.write

def solve():
    n,k=mii();b=0;a=sorted(lii())
    for i in range(k):
        b+=a[i]
    print(b)

for _ in range(1):
    solve()