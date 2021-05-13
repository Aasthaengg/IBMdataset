n = int(input())
s = input()
Z = [0 for _ in range(n)]
ans = 0
for begin in range(n):
    Z[begin] = n-begin
    i = begin + 1
    j = 0
    while i < n:
        while i+j < n and s[begin+j] ==s[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < n and k+Z[begin+k] < j:
            Z[i+k] = Z[begin+k]
            k += 1
        i += k
        j -= k
    for i in range(begin,n):
        l = min(i-begin,Z[i])
        ans = max(ans,l)
print(ans)
