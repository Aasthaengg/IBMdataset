import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    x = I()

    for a in range(-118,119+1):
        for b in range(-119,118+1):
            if a**5-b**5==x:
                break
        if a**5-b**5==x:
            break
    print(a,b)
main()            
