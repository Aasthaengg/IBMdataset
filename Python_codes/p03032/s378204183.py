N, K = map(int, input().split())
V = list(map(int, input().split()))

max_value = 0
for num_take in range(min(N, K)+1):
    max_put = min(K - num_take, max(num_take-1, 0))
    for i in range(num_take+1):
        deque = list(V)
        gems = []
        left_right = [0 for _ in range(i)] + [1 for _ in range(num_take-i)]
        for which in left_right:
            if len(deque) > 0:
                if which == 0:
                    gems.append(deque.pop(0))
                else:
                    gems.append(deque.pop(-1))
        gems.sort()

        value = max([sum(gems[num_put:]) for num_put in range(max_put+1)])
        max_value = max(max_value, value)
        
print(max_value)