import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    S = input()
    w = int(input())
    ans = []
    for i in range(0,len(S),w):
        ans.append(S[i])
    print(''.join(ans))
if __name__ == '__main__':
    main()