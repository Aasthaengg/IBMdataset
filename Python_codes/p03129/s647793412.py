N, K = [int(s) for s in input().split(' ')]
x = 0
if N%2:
    x = (N + 1) / 2
else:
    x = N/ 2
if x>=K:
    print("YES")
else:
    print("NO")