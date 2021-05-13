import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    semai = float("inf")
    for _ in range(5):
        minute = I()
        semai = min(semai,minute)
    
    group = (n+semai-1)//semai
    ans = group + 4
    print(ans)
main()