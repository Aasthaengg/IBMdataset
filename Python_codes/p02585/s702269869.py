n, k = map(int, input().split())
p = [int(i) - 1 for i in input().split()]
c = list(map(int, input().split()))

def mymax(max_variable, candidate):
    if max_variable is None:
        return candidate
    else:
        return max(max_variable, candidate)

max_cost = None
for start in range(n):
    seen = []
    next_ = p[start]
    cost_sum = []
    cost = 0
    while next_ != start:
        seen.append(next_)
        cost += c[next_]
        cost_sum.append(cost)
        next_ = p[next_]

    seen.append(start)
    cost += c[start]
    cost_sum.append(cost)

    l = len(seen)
    s = cost_sum[-1]
    for end in range(len(seen)):
        moves = end + 1
        remain_moves = k - moves
        if remain_moves < 0:
            continue
        cand_cost = cost_sum[end] + max(0, s) * int(remain_moves / l)
        max_cost = mymax(max_cost, cand_cost)
print(max_cost)

