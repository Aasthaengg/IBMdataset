n,k = list(map(int, input().split()))
h = sorted([int(input()) for _ in range(n)])

print(min([b-s for s,b in zip(h, h[k-1:])]))