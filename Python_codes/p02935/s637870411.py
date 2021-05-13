N = int(input())
V = sorted(list(map(int, input().split())), reverse=True)
while len(V) > 1:
    V.append((V.pop() + V.pop()) / 2)
print(V[0])
