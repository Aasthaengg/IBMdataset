n = int(input())
arr = list(map(int,input().split()))
last,ans = 0,0
for c in arr:
    if c < last:
        ans += (last-c)
    else:
        last = c
print(ans) 