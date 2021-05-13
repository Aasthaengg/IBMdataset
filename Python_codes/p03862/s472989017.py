N, x = map(int, input().split())
a1 = list(map(int, input().split()))
a2 = a1[::-1]
ans1 = 0
ans2 = 0

for i in range(N-1):
    tmp = a1[i] + a1[i+1] - x
    if tmp <= 0:
        continue
    red = min(a1[i+1], tmp)
    a1[i+1] -= red
    ans1 += red
    if red < tmp:
        a1[i] -= tmp-red
        ans1 += tmp-red
    
for i in range(N-1):
    tmp = a2[i] + a2[i+1] - x
    if tmp <= 0:
        continue
    red = min(a2[i+1], tmp)
    a2[i+1] -= red
    ans2 += red
    if red < tmp:
        a2[i] -= tmp-red
        ans2 += tmp-red
print(min(ans1, ans2))