n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
for vv, cc in zip(v, c):
    if vv-cc>0:
        ans += vv-cc
print(ans)