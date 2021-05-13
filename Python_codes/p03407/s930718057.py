import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    a,b,c=map(int, input().split())
    if a+b<c:
        print("No")
    else:
        print("Yes")

main()