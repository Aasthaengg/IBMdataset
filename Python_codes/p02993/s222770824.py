import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    
    bad = False
    for i in range(3):
        if S[i] == S[i+1]:
            bad = True
            break
            
    if bad:
        print('Bad')
    else:
        print('Good')
    
    return


if __name__ == '__main__':
    main()
