R, G, B = map(int, input().split())
K = int(input())

for i in range(K):
    ng = i
    nb = K-i
    g = G * 2 ** ng
    b = B * 2 ** nb
    if R < g < b:
        print("Yes")
        break
else:
    print("No")
