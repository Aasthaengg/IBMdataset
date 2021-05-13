r, c = map(int,input().split())
ans = [0 for i in range(c+1)]
for i in range(r):
    l = list(map(int, input().split()))
    l.append(sum(l))
    ans = [x + y for (x, y) in zip(ans, l)]
    print(" ".join(map(str,l)))
print(" ".join(map(str,ans)))