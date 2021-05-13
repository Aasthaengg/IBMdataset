N, C = map(int, input().split())

X = [0]
V = [0]
sV = [0]
Amax1 = [0]
Amax2 = [0]
for _ in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)
    sV.append(sV[-1]+v)
    Amax1.append(max(Amax1[-1], sV[-1]-x))
    Amax2.append(max(Amax2[-1], sV[-1]-2*x))
X.append(C)

ans = 0
for b in range(1, N+2):
    # O -> A -> B
    a1 = Amax2[b-1]+sV[-1]-sV[b-1]-(C-X[b])

    # O -> B -> A
    a2 = Amax1[b-1]+sV[-1]-sV[b-1]-2*(C-X[b])

    ans = max(ans, a1, a2)

print(ans)
