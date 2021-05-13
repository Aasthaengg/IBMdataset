N, K = [int(s) for s in input().split(' ')]
H = [int(s) for s in input().split(' ')]
print(len([h for h in H if h >= K]))
