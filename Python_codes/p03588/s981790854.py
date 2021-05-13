n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])
ab = sorted(ab, key=lambda x: -x[0])
print(ab[0][0]+ab[0][1])