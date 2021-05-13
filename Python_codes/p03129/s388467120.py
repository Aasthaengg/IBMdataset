# 1
# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a
N,K=map(int,input().split())
print('YES' if N-K-(K-1)>=0 else 'NO')