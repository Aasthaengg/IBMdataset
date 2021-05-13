import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))

##ノードの数を増やせるだけ増やす##
non_leaf_node = []
tmp = 1
for i in range(0,N+1):
    tmp = tmp -A[i]
    if tmp < 0:#頂点数が0以下になってはいけない
        print(-1)
        exit()
    non_leaf_node.append(tmp)
    tmp *= 2
non_leaf_node[-1]=0
##後ろ側から頂点の最大数を足し上げる##
##頂点数=node[i] = (non_leaf_node[i+1]+A[i+1] または non_leaf_node[i]+leaf[i])+leaf


ans = A[-1]
for i in range(N-1,-1,-1):
    non_leaf_node[i] = min(non_leaf_node[i],non_leaf_node[i+1]+A[i+1])
    ans += non_leaf_node[i]+A[i]
print(ans)
