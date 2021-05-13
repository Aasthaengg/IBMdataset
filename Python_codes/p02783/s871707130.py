#https://atcoder.jp/contests/abc153/tasks/abc153_a
M,N =map(int,input().split())
a,b = divmod(M,N)
if b == 0:
    print(a)
else:
    print(a+1)