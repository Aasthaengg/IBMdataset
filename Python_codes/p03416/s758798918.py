A, B = map(int, input().split())

ans = 0
for i in range(A,B+1):
    s = str(i)
    N = len(s)-1
    l = (len(s) // 2) + 1
    for j in range(l):
        if s[j] == s[N-j]:
            continue
        else:
            break
    else:
        ans += 1

print(ans)
