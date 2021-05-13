import sys

def main():
    N = int(input())
    A = int(input())
    x = N % 500
    if x<=A:
        print('Yes')
    else:
        print('No')

main()