N = int(input())
P = list(map(int,input().split()))

Q = [i+1 for i in range(N)]
for i in range(N):
    for j in range(i,N):
        P[i], P[j] = P[j], P[i]

        if P == Q:
            print("YES")
            exit()

        P[i], P[j] = P[j], P[i]

print("NO")