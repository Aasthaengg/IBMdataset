n,m,c = map(int, input().split())
brr = list(map(int, input().split()))
ans = 0
for i in range(n):
    s = 0
    arr = list(map(int, input().split()))
    for x,y in zip(arr, brr):
        s += x*y
    s += c
    if s > 0:
        ans += 1
print(ans)