import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1

def main():
    n,a,b=map(int, input().split())
    mx=min(a,b)
    mn=max(a+b-n,0)
    print(mx,mn)

main()