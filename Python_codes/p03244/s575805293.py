n = int(input())
v = [0] + list(map(int, input().split()))

odd = [v[i] for i in range(1, n+1, 2)]
even = [v[i] for i in range(2, n+1, 2)]

from collections import Counter
counter_odd = dict(Counter(odd))
counter_even = dict(Counter(even))

counter_odd[0] = 0
counter_even[0] = 0

counter_odd = list(counter_odd.items())
counter_even = list(counter_even.items())

counter_odd.sort(reverse=True, key=lambda x: x[1])
counter_even.sort(reverse=True, key=lambda x: x[1])

max_odd = counter_odd[0]
max_even = counter_even[0]

if max_odd[0] != max_even[0]:
    ans = len(odd) - max_odd[1] + len(even) - max_even[1]
    print(ans)
else: 
    semi_max_odd = counter_odd[1]
    semi_max_even = counter_even[1]
    loss_odd = max_odd[1] - semi_max_odd[1]
    loss_even = max_even[1] - semi_max_even[1]
    if loss_odd < loss_even:
        ans = len(odd) - semi_max_odd[1] + len(even) - max_even[1]
    else:
        ans = len(odd) - max_odd[1] + len(even) - semi_max_even[1]
    print(ans)
