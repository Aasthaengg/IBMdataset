N, K, Q = map(int, input().split())
n = [K] * N

for i in range(Q):
    A = int(input())
    n[A - 1] += 1

for result in n:
    if result - Q > 0:
        print("Yes")
    else:
        print("No")