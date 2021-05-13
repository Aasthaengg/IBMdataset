N = int(input())


max_ = -1
min_flow = float('inf')
for i in range(5):
    x = int(input())
    min_flow = min(min_flow, x)

    q, r = divmod(N, min_flow)

    if r != 0:
        q += 1

    max_ = max(max_, i + q)


print(max_)
