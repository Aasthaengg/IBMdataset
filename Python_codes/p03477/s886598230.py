import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    a,b,c,d=map(int, input().split())
    if a+b>c+d:
        print("Left")
    elif a+b==c+d:
        print("Balanced")
    else:
        print("Right")

main()