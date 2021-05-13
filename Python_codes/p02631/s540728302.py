import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    s = 0
    for a in A:
        s ^= a
    for a in A:
        print(s ^ a)
    
    

if __name__ == '__main__':
    main()

