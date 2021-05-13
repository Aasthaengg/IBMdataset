N, K = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse = True)
print(sum([l[i] for i in range(N) if i < K]))