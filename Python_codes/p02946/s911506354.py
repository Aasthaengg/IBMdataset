import sys


def input():
    return sys.stdin.readline().strip()

def main():
    k, x = map(int, input().split())
    for i in range(x-k+1,x+k):
        print(i,end=" ")
    
main()