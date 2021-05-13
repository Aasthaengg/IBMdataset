N, P = map(int, input().split())
a_li = list(map(int, input().split()))
ans = 0
o = 0
for a in a_li:
    if a % 2 != 0:
        o += 1
if o == 0:
    if P == 1:
        ans = 0
    else:
        ans = 2 ** N
else:
    ans = 2 ** (N - 1)
print(ans)
