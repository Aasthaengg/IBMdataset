n, c, k = map(int, input().split())
T = [0] * n
for i in range(n):
    T[i] = int(input())
 
T.sort()
ans, s, m = 0, 0, 0
 
for t in T:
    if m == 0:
        s = t
        m = 1
        ans += 1
    else:
        if t <= s + k:  # kill me now
            m += 1
        else:
            s = t
            m = 1
            ans += 1
    if m == c:
        m = 0
 
print(ans)