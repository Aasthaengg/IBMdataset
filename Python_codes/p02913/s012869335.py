n = int(input())
s = input()

def z_algorythm(s):
    n = len(s)
    LCP = [0]*n
    c = 0
    for i in range(1, n):
        if i + LCP[i-c] < c + LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and s[j] == s[i+j]:
                j += 1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP

ans = 0
for i in range(n):
    LCP = z_algorythm(s[i:])
    for j, l in enumerate(LCP):
        if j >= l:
            ans = max(ans, l)
print(ans)