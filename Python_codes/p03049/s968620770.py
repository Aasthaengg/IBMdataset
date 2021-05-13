N = int(input())
both = 0 
cnt = 0
gA = 0
sB = 0
for _ in range(N):
    s = input()
    cnt += s.count('AB')
    if s[-1] == 'A': gA += 1
    if s[0] == 'B': sB += 1
    if s[0] == 'B' and s[-1] == 'A': both += 1
ans = min(gA, sB) + cnt
if both == gA and gA == sB and both != 0:
    ans -= 1
print(ans)
# print(cnt, gA, sB, both)
