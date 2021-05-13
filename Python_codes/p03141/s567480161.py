n = int(input())
AB = [tuple(int(x) for x in input().split()) for _ in range(n)]
C = sorted(AB, key=lambda x: x[0] + x[1], reverse=True)
print(sum(a for a, b in C[::2]) - sum(b for a, b in C[1::2]))
