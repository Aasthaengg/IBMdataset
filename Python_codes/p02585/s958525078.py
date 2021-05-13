def D():
    N, K = map(int, input().split())
    P = [int(n) for n in input().split()]
    C = [int(n) for n in input().split()]
    cycle_sums = [float('-inf')]*N
    cycle_length = [-1]*N
    for i in range(N):
        # every element is guaranteed to be in a cycle
        if cycle_sums[i] == float('-inf'): #have not been processed, g
            points = 0
            visited_set = set()
            visited_order = []
            while P[i] not in visited_set:
                visited_set.add(P[i])
                visited_order.append(P[i])
                i = P[i]-1
            _sum = 0
            for j in range(len(visited_order)):
                _sum += C[visited_order[j]-1]
            for j in range(len(visited_order)):
                cycle_sums[visited_order[j]-1] = _sum
                cycle_length[visited_order[j]-1] = len(visited_order)
    #print(cycle_sums, cycle_length)

    ans = float('-inf')
    for j in range(N):
        i = j
        k = K
        points = 0
        if cycle_sums[i] > 0:
            num_cycles, remainder = divmod(k, cycle_length[i])
            if num_cycles > 0:
                num_cycles -= 1
                remainder += cycle_length[i]
            points += cycle_sums[i] * num_cycles
            k = remainder
        else:
            #make at least one move
            i = P[i]-1
            points += C[i]
            k = min(k, cycle_length[i]-1)
        #print(j, points)
        _sum = points

        while k > 0:
            i = P[i]-1
            _sum += C[i]
            points = max(points, _sum)
            k -= 1
        #print(j, points)
        ans = max(ans, points)

    return ans
        # visited_dict = {}
        # visited_order = []
        # while K > 0 and P[i] not in visited_dict:
        #     visited_dict[P[i]] = len(visited_order)
        #     visited_order.append(P[i])
        #     i = P[i]-1
        #     points += C[i]
        # if K > 0: #cycle found
        #     cycle_len = len(visited_order) - visited_dict(P[i])
        #     num_cycles_left, remainder = divmod(K, cycle_len)
        #     _sum = 0
        #     for j in range(visited_dict(P[i]), len(visited_order)):
        #         _sum += C[visited_order[j]]
        #         if j - visited_dict(P[i]) == remainder-1:
        #             points += _sum
        #     points += num_cycles_left*_sum

print(D())