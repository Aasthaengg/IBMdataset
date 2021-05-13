N, K, Q = map(int, input().split())

point = [0] * N

for _ in range(Q):
    A = int(input())
    point[A - 1] += 1

for point in point:
    if Q - point < K:
        print("Yes")
    else:
        print("No")