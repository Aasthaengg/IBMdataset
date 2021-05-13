S = input()
prev = ""
cut = [0]
inds = []
rs = []
r = 0
for i in range(len(S)):
    if prev == "L" and S[i] == "R":
        cut.append(i)
    if prev == "R" and S[i] == "L":
        inds.append(i)
        rs.append(r)
        r = 0
    if S[i] == "R":
        r += 1
    prev = S[i]
cut.append(len(S))
diff = [cut[i]-cut[i-1] for i in range(1,len(cut))]
ans = [0] * len(S)
# print(rs)
# print(diff)
# print(inds)
for d, i, r in zip(diff, inds, rs):
    ans[i-1] = d//2 
    ans[i] = d//2
    if d%2 == 1 and r%2==1:
        ans[i-1] += 1
    elif d%2 == 1 and r%2 == 0:
        ans[i] += 1
print(*ans)