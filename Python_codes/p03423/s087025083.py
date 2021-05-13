import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
int1 = lambda x: int(x) - 1

def main():
    n=int(input())
    print(n//3)

main()