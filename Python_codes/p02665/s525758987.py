import sys
import math
n = int(input())
A = list(map(int, input().split()))
NODE_RANGE = [0 for i in range(n+1)]
NODE_RANGE[n] = [A[n], A[n]]
NODE_MAX = [0 for i in range(n+1)]
NODE_MAX[0]=1
# d=nから見ていって、各dに対するノードの最小値、最大値を求める
for i in range(n-1, -1, -1):
    node_min = math.ceil( NODE_RANGE[i+1][0]/2 ) + A[i]
    node_max = NODE_RANGE[i+1][1] + A[i]
    NODE_RANGE[i]=[node_min, node_max]

if NODE_RANGE[0][0] > 1 or 1 > NODE_RANGE[0][1]: # d=0の時のノード数は1
    print(-1)
    sys.exit()

# print(NODE_RANGE)
# d=0から最大ノード数を確定させていく
for i in range(1, n+1):
    NODE_MAX[i] = min((NODE_MAX[i-1]-A[i-1])*2, NODE_RANGE[i][1])
    # print(NODE_MAX[i-1] + A[i], NODE_RANGE[i][1])
# print(NODE_MAX)
print(sum(NODE_MAX))