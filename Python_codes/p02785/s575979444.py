#https://atcoder.jp/contests/abc153/tasks/abc153_c
N,K =map(int,input().split())
M_List = sorted(list(map(int,input().split())))
if K == 0:
    print(sum(M_List))
elif N<=K:
    print(0)
else:
    print(sum(M_List[:K*(-1)]))