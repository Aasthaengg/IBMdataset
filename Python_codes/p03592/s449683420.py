import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m, k = LI()
    for i in range(n):
        for j in range(m+1):
            if i*m + j*(n-2*i) == k:
                print("Yes")
                exit(0)
    else:
        print("No")
main()
