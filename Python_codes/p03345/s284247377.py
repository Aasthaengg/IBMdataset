# 4
# https://atcoder.jp/contests/agc024/tasks/agc024_a
A,B,C,K=map(int,input().split())
K%=2
p=A-B
p*=(-1)**K
print(p if p<=10**18 else 'Unfair')
