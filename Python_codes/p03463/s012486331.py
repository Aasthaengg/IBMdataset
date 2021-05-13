import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, A, B = [int(x) for x in input().split()]

    if (B - A) % 2 == 1:
        print("Borys")
    else:
        print("Alice")

    
    
    

if __name__ == '__main__':
    main()

