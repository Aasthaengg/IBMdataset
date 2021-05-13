N = int(input())
V = list(map(int, input().split()))
V.sort()

for n in range(N-1):
    x = V.pop(0)
    y = V.pop(0)
    V.append((x+y)/2)
    V.sort()
print(V[0])