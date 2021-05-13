# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)
import collections
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def fi(): return float(input())
def mfi(): return map(float, input().rstrip().split())
def lmfi(): return list(map(float, input().rstrip().split()))
def li(): return list(input().rstrip())
def debug(*args, sep=" ", end="\n"): print("debug:", *args, file=sys.stderr, sep=sep, end=end) if not __debug__ else None
def exit(*arg): print(*arg); sys.exit()
# template

def reverse(s: str):
    return s[::-1]

def main():
    S = input().rstrip()
    # ss = set()
    # ss.add(S)
    # for K in range(2, len(S) + 1):
    #     for i in range(len(S) - K + 1):
    #         news = ''.join([S[0:i], reverse(S[i:i + K]), S[i + K:]])
    #         print(news, i, K, end="")
    #         if news not in ss:
    #             ss.add(news)
    #             print("")
    #         else:
    #             print("*")
    # print(len(ss))
    d = collections.defaultdict(int)
    for x in S:
        d[x] += 1
    # print(d)
    minum = 0
    for i in d:
        minum += d[i] * (d[i] - 1) // 2
    print(len(S) * (len(S) - 1) // 2 - minum + 1)
    return


if __name__ == '__main__':
    main()
