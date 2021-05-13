n = int(input())

ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((b, a))
    
ab.sort()

print(ab[0][0] + ab[0][1])