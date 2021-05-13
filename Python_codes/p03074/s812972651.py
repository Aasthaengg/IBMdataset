n, k = map(int, input().split())
s = list(input())


L = [0]
R = []
for i, (a, b) in enumerate(zip(s, s[1:])):
    if (a, b) == ('0', '1'):
        L.append(i+1)

    if (a, b) == ('1', '0'):
        R.append(i)
else:
    R.append(n-1)

ans = R[0]-L[0]+1
if s[0] == '0':
    k -= 1
k = min(k, len(R)-1)
for l, r in zip(L, R[k:]):
    x = r-l+1
    if ans < x:
        ans = x
print(ans)
