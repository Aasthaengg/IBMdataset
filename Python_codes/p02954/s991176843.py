from math import ceil
S = input()
ans = [0]*len(S)
cnt = 1
tmp = S[0]
pos = 0
for n,i in enumerate(S[1:],1):
    if i == tmp:
        cnt += 1
    if i == 'R' and i != tmp:
        ans[pos] = cnt
        cnt = 1
        tmp = i
    if i == 'L' and i != tmp:
        ans[n] = cnt
        pos = n-1
        cnt = 1
        tmp = i
if i == 'L':
    ans[pos] = cnt
else:
    ans[-1] = cnt
i = 0
while i < len(S):
    if ans[i]:
        ans[i],ans[i+1] = ceil(ans[i+1]/2)+ans[i]//2,ceil(ans[i]/2)+ans[i+1]//2
        i += 2
    else:
        i += 1
print(' '.join(list(map(str,ans))))