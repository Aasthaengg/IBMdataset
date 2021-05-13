m, k = map(int, input().split())
if m==1 and k==0:
    print(0,0,1,1)
    exit()
if m==k==1:
    print(-1)
    exit()

if 2**m<=k:
    print(-1)
    exit()
ans = [k]
for i in range(2**m):
    if i != k:
        ans.append(i)
ans.append(k)
for i in reversed(range(2**m)):
    if i != k:
        ans.append(i)
print(*ans)
