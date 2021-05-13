N = int(input())
bmin = 10000000000
ans = 0
for i in range(N):
    a,b = map(int,input().split())
    if b < bmin:
        bmin = b
        ans = a + bmin
print(ans)