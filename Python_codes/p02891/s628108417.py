S = input()
k = int(input())

prev = S[0]
cnt = 0
for i in range(1,len(S)):
    if prev == S[i]:
        cnt += 1
        prev = "$"
        continue
    prev = S[i]

ans = k*cnt

if S[0] == S[-1]:
    m = 0
    for s in S:
        if s == S[0]:
            m += 1
        else:
            break
    a = 0
    for s in S[::-1]:
        if s == S[-1]:
            a += 1
        else:
            break
    if a%2 and m%2:
        ans += k-1
if len(set(S)) == 1:
    ans = (len(S)*k//2)
print(ans)