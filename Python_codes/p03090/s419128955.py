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
    group_cnt = -(-N//2)
    group_sum = N if N % 2 == 1 else N+1
    s = (group_cnt - 1) * group_sum
    edge = set()
    loop_num = group_cnt if N % 2 == 0 else group_cnt - 1
    for comb in combinations(range(1, loop_num+1), 2):
        for i in (comb[0], group_sum-comb[0]):
            for j in (comb[1], group_sum-comb[1]):
                edge.add((i, j))
    if N % 2 == 1:
        for i in range(1, N):
            edge.add((i, N))
    print(len(edge))
    for e in edge:
        print(*e)
    #print(check(edge, s))

main(N)
