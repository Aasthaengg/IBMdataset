n = int(input())
l = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append((a+b,a,b))
l = sorted(l,reverse=True)
takahashi = 0
aoki = 0
for i in range(n):
    if i%2:
        aoki+=l[i][2]
    else:
        takahashi+=l[i][1]
print(takahashi-aoki)