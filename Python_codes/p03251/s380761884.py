N, M, X, Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

ans = 'War'
Z = [i for i in range(X+1, Y+1)]
z = [i for i in range(max(x)+1, min(y)+1)]

for i in Z:
    if i in z:
        ans = 'No War'
        break

print(ans)
