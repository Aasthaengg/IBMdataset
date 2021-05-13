import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
sys.setrecursionlimit(10**7)

def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    N = I()
    kuku_list = []
    for i in range(1,10):
        for j in range(1,10):
            kuku_list.append(i*j)
    print("Yes" if N in kuku_list else "No")

main()

