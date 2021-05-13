s = input()
n = len(s)

ans = 0

for i in range(n):
    k = 0
    l = 0
    while i + k < n:
        if s[i+k] == 'A' or s[i+k] == 'C' or s[i+k] == 'G' or s[i+k] == 'T':
            k += 1
            l += 1
        else:
            break
    ans = max(ans, l)

print(ans)