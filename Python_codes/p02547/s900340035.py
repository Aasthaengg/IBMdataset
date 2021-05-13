n = int(input())
d = [input().split() for _ in range(n)]
if any(i[0]==i[1] and j[0]==j[1] and k[0]==k[1] for i, j, k in zip(d, d[1:], d[2:])):
    print('Yes')
else:
    print('No')
