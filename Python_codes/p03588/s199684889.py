n = int(input())
L = [[0, 0] for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    L[i][0] = a
    L[i][1] = b

L.sort(reverse=True)
print(L[0][0]+L[0][1])
