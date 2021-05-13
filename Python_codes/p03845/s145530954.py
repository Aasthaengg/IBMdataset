n = int(input())
t = list(map(int,input().split()))
t.insert(0,0)
m = int(input())
for i in range(m):
    p,x = map(int,input().split())
    ans = sum(t) - t[p] + x
    print(ans)
