N = int(input())
h = []
for _ in range(N) :
    A, B = map(int, input().split())
    h.append((A + B, A, B))
    
h.sort(reverse=True)
print(sum([h[i][1] for i in range(0, N, 2)]) - sum([h[i][2] for i in range(1, N, 2)]))