# ABC 79
def main():
    MAX = 10**6
    H,W = list(map(int, input().split()))
    costs = [list(map(int, input().split())) for i in range(10)]
    to_ones = [MAX] * 10
    to_ones[1] = 0
    visited = set([1])
    un_visited = set([i for i in range(10)])
    un_visited.remove(1)

    while len(un_visited) > 0:
        target = 0
        min_val = MAX
        for i in visited:
            for j in un_visited:
                if costs[j][i] < min_val:
                    min_val = costs[j][i]
                    target = j

        visited.add(target)
        un_visited.remove(target)
        to_ones[target] = min_val

        for x in un_visited:
            costs[x][target] += min_val
        
    A_cnts = [0] * 11 # -1 -> 10

    for i in range(H):
        A = list(map(int, input().split()))
        for a in A:
            A_cnts[a] += 1
    
    res = 0
    for i in range(10):
        if i == 1:
            continue
        res += A_cnts[i] * to_ones[i]

    print(res)


if __name__ == "__main__":
    main()