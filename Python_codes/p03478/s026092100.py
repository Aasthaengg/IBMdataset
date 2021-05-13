n,a,b = map(int, input().split())
l = []

for i in range(1,n+1):
    if a <= sum([int(j) for j in list(str(i))]) <= b:
        l.append(i)

print(sum(l))