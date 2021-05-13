A, B = map(int, input().split())
ans = 0
for i in range(A, B + 1):
    a = str(i)
    a_len = len(a)
    a_len_mid = len(a) // 2
    pre = a[:a_len_mid]
    pos = ''.join(list(reversed(a[(a_len_mid + 1):a_len])))
    #if pre in pos:
    if pos.startswith(pre):
        ans += 1
print(ans)
