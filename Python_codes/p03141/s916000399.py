N = int(input())
A, B, AB = [], [],  []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append(a + b)
AB.sort(reverse=True)
print(sum(AB[::2]) - sum(B))
