l = list(map(int, input().split()))
K = int(input())

idx = l.index(max(l))
l[idx] = pow(2, K) * l[idx]
print(sum(l))