N = int(input())
P = list(map(int,input().split()))

if all(a<b for a,b in zip(P,P[1:])):
    print('YES')
    exit()

for i in range(N-1):
    for j in range(i+1, N):
        P[i],P[j] = P[j],P[i]
        if all(a<b for a,b in zip(P,P[1:])):
            print('YES')
            exit()
        P[i],P[j] = P[j],P[i]
print('NO')