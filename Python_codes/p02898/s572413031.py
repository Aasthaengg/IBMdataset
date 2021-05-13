N,K = map(int, input().split())
H = map(int, input().split())

print(sum([i >= K for i in H]))