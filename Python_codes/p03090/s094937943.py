from itertools import combinations
N = int(input())

def check(edge, s):
    nodes = [0] * (N+1)
    for a, b in edge:
        nodes[a] += b
        nodes[b] += a
    return all([s == i for i in nodes[1:]])

def main(N):
    # 合計になる2頂点のグループを作って、その塊でつないでいく
    group_sum = N if N % 2 == 1 else N+1
    edge = set()
    for i in range(1,N+1):
        for j in range(i+1, N+1):
            if i+j == group_sum: continue
            edge.add((i,j))
    print(len(edge))
    for e in edge:
        print(*e)

main(N)
