import sys
n = int(input())
a = list(map(int, input().split()))

max_edge_num = pow(2,n)

if a[0] > 0 and n>0:
    print(-1)
    sys.exit()
if a[0] == 1 and n==0:
    print(1)
    sys.exit()
elif a[0] > 1 and n == 0:
    print(-1)
    sys.exit()

total_lost = 0
remained_alls = [1]

for depth in range(1,n+1):
    total_lost *= 2
    full_nodes = pow(2,depth)
    remained_nodes = full_nodes - total_lost
    remained_alls.append(remained_nodes)
    if a[depth] > remained_nodes:
        print(-1)
        sys.exit()
    else:
        total_lost += a[depth]

max_nodes_all = [a[n]]

for depth in range(n-1,0,-1):
    possible = max_nodes_all[-1]
    now = min(possible+a[depth],remained_alls[depth])
    max_nodes_all.append(now)

max_nodes_all.append(1)

answer = 0
for nodes in max_nodes_all:
    answer+=nodes

print(answer)