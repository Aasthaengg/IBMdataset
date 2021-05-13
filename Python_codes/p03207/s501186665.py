N = int(input())
L = [int(input()) for _ in range(N)]
L.sort()
L[-1] = L[-1] // 2
print(sum(L))