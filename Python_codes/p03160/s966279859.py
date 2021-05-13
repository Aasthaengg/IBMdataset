N = int(input())
h = [int(x) for x in input().split()]

Cost = [0] * N
Cost[1] = abs(h[1] - h[0])

for i in range(2, N):
    Cost[i] = min(Cost[i - 1] + abs(h[i] - h[i - 1]), Cost[i - 2] + abs(h[i] - h[i - 2]))

print(Cost[-1])