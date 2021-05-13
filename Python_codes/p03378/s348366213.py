N, M, X = map(int, input().split())
A = [int(i) for i in input().split()]

distance_to_head = len([i for i in A if i < X])
distance_to_tail = len([i for i in A if X < i])
print(min(distance_to_head, distance_to_tail))