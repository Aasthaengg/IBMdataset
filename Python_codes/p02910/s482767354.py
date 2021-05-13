import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    S = readline().strip()
    
    odd = {'R', 'U', 'D'}
    even = {'L', 'U', 'D'}
    
    ans = 'Yes'
    for i, c in enumerate(S):
        if not i % 2 and c not in odd:
            ans = 'No'
        elif i % 2 and c not in even:
            ans = 'No'
    
    print(ans)
    return


if __name__ == '__main__':
    main()
