n, k = list(map(int, input().split()))
s = list(input())

t = [s[0]]

for i in range(1, n):
    if s[i-1] != s[i]:
        t.append(s[i])

#print(t)

a = 0

if len(t) <= 2 * k:
    a = n-1
else:
    a = (n-1) - (len(t) - 1 - 2 * k)

print(a)
