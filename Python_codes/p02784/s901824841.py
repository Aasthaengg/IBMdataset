#https://atcoder.jp/contests/abc153/tasks/abc153_b
M,N =map(int,input().split())
N_List = list(map(int,input().split()))

if sum(N_List) < M:
    print("No")
else:
    print("Yes")
