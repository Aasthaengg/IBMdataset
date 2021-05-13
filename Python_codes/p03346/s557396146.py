N = int(input())
P = []
Q = [0 for i in range(N+1)]
for i in range(1, N+1):
    Q[int(input())] = i

straight = 1
max_straight = 1
for i in range(1, N):
    if Q[i] < Q[i+1]:
        straight += 1
        max_straight = max(straight, max_straight)
    else:
        straight = 1

print(N - max_straight)