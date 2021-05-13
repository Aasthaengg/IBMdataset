n,m = map(int, input().split())
l = [i for i in range(1,m+1)]
l2 = []
for _ in range(n):
    k = list(map(int, input().split()))
    del k[0]
    for i in range(len(l)):
        if l[i] not in k:
            l2.append(l[i])
l2 = list(set(l2))
print(len(l)-len(l2))