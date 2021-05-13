n,y = map(int, input().split())


s = [-1,-1,-1]

for i in range(n+1):
    for j in range(n+1-i):
        if 10000*i + 5000*j +1000*(n-i-j) == y:
            s = [i,j,n-i-j]
            break

print(*[x for x in s])