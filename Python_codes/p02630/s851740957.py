n = int(input())
a = list(map(int,input().split()))
tmp = [0] * 100001
ans = 0
for i in range(n):
    tmp[a[i]] += 1
    ans += a[i]
q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    ans -= x * tmp[x]
    ans += y * tmp[x]
    tmp[y] += tmp[x]
    tmp[x] = 0
    print(ans)
