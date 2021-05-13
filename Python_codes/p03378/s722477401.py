N, M, X = map(int, input().split())
A = [int(i) for i in input().split()]

distance_to_head = len(list(filter(lambda x: X < x, A)))
distance_to_tail = len(list(filter(lambda x: x < X, A)))
print(min(distance_to_head, distance_to_tail))