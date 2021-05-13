n, k = map(int, input().split())
s = input()

prev_R = '1'
for R in range(n):
    if (prev_R, s[R]) == ('1', '0'):
        k -= 1
        if k < 0:
            R -= 1
            break
    prev_R = s[R]

ans = R+1
for L in range(n-1):
    if (s[L], s[L+1]) != ('0', '1'):
        continue
    R += 1
    while R < n-1 and (s[R], s[R+1]) != ('1', '0'):
        R += 1
    if ans < R-L:
        ans = R-L
print(ans)