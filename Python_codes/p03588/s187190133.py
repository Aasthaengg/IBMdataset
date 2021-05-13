n = int(input())
rank = []
point = []
for _ in range(n):
    a,b = map(int,input().split())
    rank.append(a)
    point.append(b)
print (max(rank) + point[rank.index(max(rank))])