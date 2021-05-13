n = int(input())
s = str(input())

def z_algorithm(s):
    n = len(s)
    Z = [0]*n
    Z[0] = n
    i = 1
    j = 0
    while i < n:
        while i+j < n and s[j] == s[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < n and k+Z[k] < j:
            Z[i+k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z

s = list(s)
s.reverse()
import copy
ans = 0
for i in range(n):
    if i != 0:
        s.pop()
    t = copy.copy(s)
    t.reverse()
    t = ''.join(t)
    Z = z_algorithm(t)
    for i, z in enumerate(Z):
        ans = max(ans, min(i, z))
print(ans)
