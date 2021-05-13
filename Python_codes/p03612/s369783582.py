N = int(input())
P = list(map(int, input().split()))
c = 0
for i in range(N):
    f = 1
    if P[i] == i+1:
        if i != N - 1:
            if P[i+1] != i+1:
                t = P[i]
                P[i] = P[i+1]
                P[i+1] = t
                c += 1
        else:
            if P[i-1] != i+1:
                t = P[i]
                P[i] = P[i-1]
                P[i-1] = t
                c += 1
print(c)
