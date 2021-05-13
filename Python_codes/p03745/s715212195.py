N = int(input())
A = list(map(int,input().split()))
up = dn = False
ans = 1
p = A[0]
for a in A:
    if p < a:
        up = True
    elif p > a:
        dn = True
    if up and dn:
        ans += 1
        up = dn = False
    p = a
print(ans)