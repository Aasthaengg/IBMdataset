import sys
def input():
    return sys.stdin.readline()[:-1]

N,M,P = list(map(int,input().split()))
 
e_list = []
for i in range(M):
    A,B,C = list(map(int,input().split()))
    A,B = A-1,B-1
    e_list.append((A,B,P-C))
    
 
#ベルマンフォード法
#e_listの用意
vi=0
min_dis_list = [10**27]*N
min_dis_list[vi] = 0
 
for i in range(N-1):
    for e in e_list:
        u,v,d = e
        if min_dis_list[v]>min_dis_list[u]+d:
            min_dis_list[v]=min_dis_list[u]+d
 
neg_loop_flag=[False]*N
 
for i in range(N):
    for e in e_list:
        u,v,d = e
        if min_dis_list[u] < 10**26:
            if min_dis_list[u] + d < min_dis_list[v]:
                neg_loop_flag[v]=True
                min_dis_list[v] = min_dis_list[u] + d
            if neg_loop_flag[u]:
                neg_loop_flag[v]=True
 
 
if neg_loop_flag[N-1]:
    print(-1)
else:
    print(max(0,-min_dis_list[N-1]))