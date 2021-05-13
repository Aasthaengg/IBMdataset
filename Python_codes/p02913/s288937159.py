n,s = int(input()), list(input())
def z_algo(s):
    n = len(s)
    a = [0]*n
    i,j,l = 1,0,n
    a[0] = n
    while i < l:
        while i+j < l and s[j] == s[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        a[i] = j
        k = 1
        while l-i > k < j-a[k]:
            a[i+k] = a[k]
            k += 1
        i += k
        j -= k
    return a

ans = 0
for i in range(n-1):
    a = z_algo(s[i:])
    len_a = len(a)
    for j in range(len_a):
        ans = max(ans, min(j,a[j]))
print(ans)