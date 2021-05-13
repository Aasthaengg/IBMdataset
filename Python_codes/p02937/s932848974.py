#coding:utf-8
import sys,os
from collections import defaultdict
from bisect import bisect_left
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    s = input()
    t = input()
    # 各アルファベットについてsの何文字目に現れたかを保持するリストの辞書
    alphabets = defaultdict(list)
    for i,c in enumerate(s):
        alphabets[c].append(i)
    # sの繰り返した数,周期,0-indexed
    period = 0
    # sの何文字目までを使ったか
    looking = -1
    # 各アルファベットをその周期で何回使ったかを保持する辞書
    alphabet_index = defaultdict(int)
    for i,c in enumerate(t):
        index = bisect_left(alphabets[c],looking+1, alphabet_index[c])
        # その周期で使えるアルファベットがない場合
        if index == len(alphabets[c]):
            # そのアルファベットが存在しない場合は解なし
            if len(alphabets[c]) == 0:
                print(-1)
                return
            
            # 次の周期に移る
            period += 1
            alphabet_index = defaultdict(int)
            looking = alphabets[c][0]

        else:
            looking = alphabets[c][index]

        alphabet_index[c] += 1
    print(period * len(s) + looking + 1)






    

if __name__ == '__main__':
    main()