N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]
correct = [0] * N

for a in A:
    correct[a-1] += 1

hp = Q - K
for i in range(N):
    if correct[i] > hp:
        print("Yes")
    else:
        print("No")