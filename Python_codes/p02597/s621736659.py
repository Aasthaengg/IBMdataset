N = int(input())
c = input()

R = 0
W = 0
for ci in c:
    if ci == 'R':
        R += 1

ans = max(R,W)
for ci in c:
    if ci == 'R':
        R -= 1
    else:
        W += 1
    tmp = max(R,W)
    ans = min(ans,tmp)

print(ans)