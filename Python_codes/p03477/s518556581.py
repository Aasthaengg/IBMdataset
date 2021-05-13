import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    A,B,C,D = map(int,input().split())
    A += B
    C += D
    if A > C:
        print('Left')
    elif A == C:
        print('Balanced')
    else:
        print('Right')
if __name__ == '__main__':
    main()