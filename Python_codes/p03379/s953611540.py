n = int(input())
al = list(map(int, input().split()))

als = list(sorted(al))

x = als[n//2]
y = als[n//2-1]

for i in range(n):
    z = al[i]
    if z <=y:
        print(x)
    else:
        print(y)