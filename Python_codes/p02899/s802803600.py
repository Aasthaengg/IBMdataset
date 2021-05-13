N = int(input())
A = []
for i, a in enumerate(map(int, input().split())):
    A.append((a, i))
A.sort()
print(*[i+1 for _, i in A])