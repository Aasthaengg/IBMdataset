n = int(input())
s = input()
ans = s.count('R') * s.count('G') * s.count('B')
for i in range(n):
    for j in range(i, n):
        k = j + (j - i)
        if k >= n:
            break
        if s[i] != s[j] != s[k] != s[i]:
            ans -= 1

print(ans)