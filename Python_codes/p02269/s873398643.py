import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    before = set()
    for _ in range(N):
        s,t = input().split()
        if s == 'insert':
            before.add(t)
        else:
            if t in before:
                print('yes')
            else:
                print('no')
if __name__ == '__main__':
    main()
