# 1
# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a
if False:
    N,K=map(int,input().split())
    print('YES' if N-K-(K-1)>=0 else 'NO')

# 2
# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_b
if False:
    N=int(input())
    S=input()
    print('Yes' if S.count('R')>S.count('B') else 'No')

# 3
# https://atcoder.jp/contests/exawizards2019/tasks/exawizards2019_a
if True:
    print('Yes' if len(set(input().split()))==1 else 'No')
