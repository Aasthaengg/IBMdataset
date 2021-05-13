n,k = map(int,input().split())
s = input()+"2"
lst0 = [0]
lst1 = [0]
if s[0] == "0": lst1.append(0)
cnt = 0
for i in range(n):
    cnt += 1
    if s[i] != s[i+1]:
        if s[i] == "0": lst0.append(cnt)
        else: lst1.append(cnt)
        cnt = 0
l0 = len(lst0)
l1 = len(lst1)
k = min(k,l0-1)
for i in range(l0-1): lst0[i+1] += lst0[i]
for i in range(l1-1): lst1[i+1] += lst1[i]
# print(lst0)
# print(lst1)
ans = 0
for l in range(l0):
    r = min(l+k,l0-1)
    rr = r if r == l1-1 else r+1
    cnt = lst0[r]-lst0[l] + lst1[rr]-lst1[l]
    ans = max(cnt,ans)
print(ans)