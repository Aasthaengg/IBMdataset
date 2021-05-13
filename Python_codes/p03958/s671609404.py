N = list(map(int, input().split()))
Q = list(map(int, input().split()))
maxQ = max(Q)
rest = N[0] - maxQ
print(max([maxQ-rest-1, 0]))