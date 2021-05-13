N,K=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき

if N%K==0:
    print('0')
else:
    print('1')