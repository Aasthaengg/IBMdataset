N, M = [int(i) for i in input().split()]

ans = set([i + 1 for i in range(M)])
for _ in range(N):
    T = input().split()
    A = set([int(i) for i in T[1:]])
    ans = ans & A
print(len(ans))

