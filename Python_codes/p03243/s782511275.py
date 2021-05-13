n = int(input())
N = list(str(n))
ans = str()
res = N[0]
mn = True
bl = True
for x in N:
    if int(res) < int(x):
        mn = False
    if x != res:
        bl = False
if bl:
    print(n)
else:
    if not mn:
        for i in range(len(N)):
            ans += str(int(res) + 1)
        print(ans)
    else:
        for i in range(len(N)):
            ans += str(res)
        print(ans)

