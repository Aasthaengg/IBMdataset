
def search_maximum_profit(rs):
    """
        rs: ??´??°?????????
        search max[s | s = rs[j] - rs[i] (j > i)]
        return: s
    """
    l = len(rs)
    if l <= 1:
        return None
    elif l == 2:
        return rs[1] - rs[0]
    else:
        left_profit = search_maximum_profit(rs[:l // 2])
        right_profit = search_maximum_profit(rs[l // 2:])
        left_min = min(rs[:l // 2])
        right_max = max(rs[l // 2:])
        profits = []
        if left_profit != None:
            profits.append(left_profit)
        if right_profit != None:
            profits.append(right_profit)
        profits.append(right_max - left_min)
        return max(profits)

n = int(input())
rs = []
for i in range(n):
    rs.append(int(input()))

print(search_maximum_profit(rs))