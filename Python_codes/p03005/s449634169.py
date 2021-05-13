#https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_a

N,K = [int(i) for i in input().split()]
if K > 1:
    print(N-K)
else:
    print(0)