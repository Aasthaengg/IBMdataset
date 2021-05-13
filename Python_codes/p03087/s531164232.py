n, q = map(int, input().split())
s = input()

mae = [0 for i in range(n)]
ato = [0 for i in range(n)]
bef = 'Z'
for i in range(n):
    if bef == 'A' and s[i] == 'C':
        mae[i-1] = -1
    bef = s[i]
bef = 'Z'
for i in range(n-1, -1, -1):
    if bef == 'C' and s[i] == 'A':
        ato[i+1] = -1
    bef = s[i]

for i in range(1, n):
    mae[i] += mae[i-1]
for i in range(n-2, -1, -1):
    ato[i] += ato[i+1]
num = -mae[-1]

ans = []
for i in range(q):
    li, ri = map(int, input().split())
    li, ri = li-1, ri-1
    minus = 0
    if li > 0:
        minus += mae[li-1]
    if ri < n-1:
        minus += ato[ri+1]
    ans.append(num+minus)

for i in range(q):
    print(ans[i])