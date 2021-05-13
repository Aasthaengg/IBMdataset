import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    S,W = map(int,input().split())
    print("unsafe" if S<=W else "safe")

main()
