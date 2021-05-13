n,k = map(int,input().split())
A = list(map(int,input().split()))
Ad = {}
for a in A:
    if not a in Ad:
        Ad[a] = 1
    else:
        Ad[a] += 1

if len(set(A)) == k:
    print (0)
else:
    x = len(set(A)) - k
    Ad = sorted(Ad.items(), key=lambda x:x[1])
    ans = 0
    for i in range(x):
        ans += Ad[i][1]
    print (ans)
