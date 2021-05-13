n = int(input())
li = [int(input()) for _ in range(n)]
ma = {}
for i,l in enumerate(li):
    ma[l] = i+1
nu = []
for j in range(n):
    nu.append(ma[j+1])

ans = [0]
tmp = 0
cnt = 0
for k,u in enumerate(nu):
    if k == 0:
        tmp = u
        cnt += 1
        continue
    if u > tmp:
        tmp = u
        cnt += 1
    else:
        ans.append(cnt)
        tmp = u
        cnt = 1
ans.append(cnt)
#print(ans)
#print(n,max(ans))
print(n - max(ans))