import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


def z_algorithm(s):
    """
    各iについてs[0..n)とs[i..n)のLCP(Longest Common Prefix)の長さを求める
    s: str or (list of int )
    """
    n = len(s)
    if n==0:
        return []
    z = [None]*n
    z[0] = 0
    j = 0
    for i in range(1,n):
        k = 0 if j + z[j] <= i else min(j+z[j]-i, z[i-j])
        z[i] = k
        while i+k<n and s[k]==s[i+k]:
            k += 1
        z[i] = k
        if j+z[j] < i+z[i]:
            j = i
    z[0] = n
    return z
n = int(input())
s = input()
ans = 0
for i in range(n):
    z = z_algorithm(s[i:])
    val = -1
    for j in range(len(z)):
        val = max(val, min(z[j], j))
    ans = max(ans, val)
#     print(z)
print(ans)