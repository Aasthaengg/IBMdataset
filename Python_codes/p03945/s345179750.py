import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    S = readline().decode('utf-8').strip()
    change = 0
    L = len(S)
    for i in range(1,L):
        if S[i-1]!=S[i]:
            change += 1
    print(change)

if __name__ == '__main__':
    main()