N = int(input())
vlist = list(map(int, input().split()))
clist = list(map(int, input().split()))
indi = [v - c for v, c in zip(vlist, clist)]
ans = 0
for i in indi:
    if i > 0:
        ans += i
print(ans)