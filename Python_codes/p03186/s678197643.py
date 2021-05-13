import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    a,b,c = map(int,input().split())
    if c <= a + b:
        print(b + c)
    else:
        print(a + 2*b + 1)
if __name__ == '__main__':
    main()