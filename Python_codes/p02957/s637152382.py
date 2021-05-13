import sys
import math

def input():
    return sys.stdin.readline().rstrip()


def main():
    A,B=map(int,input().split())
    
    if (A + B) %2 ==0:
        print(int(A/2+B/2))
    else:
        print("IMPOSSIBLE")
    



if __name__ == "__main__":
    main()
