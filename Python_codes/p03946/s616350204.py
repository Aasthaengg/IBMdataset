N,T = map(int,input().split())
A = list(map(int,input().split()))
mn = A[0]
gain = 0
ans = 1
for a in A[1:]:
    if a < mn:
        mn = a
        continue
    if a-mn == gain:
        ans += 1
    elif a-mn > gain:
        gain = a-mn
        ans = 1
print(ans)