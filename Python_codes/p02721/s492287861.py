n, k, c = map(int, input().split())
s = input()

left = []
right = []

i = 0
while i < n:
    if s[i] == 'o':
        left.append(i)
        i += c
        if len(left) == k:
            break
    i += 1
i = n - 1
while i >= 0:
    if s[i] == 'o':
        right.append(i)
        i -= c
        if len(right) == k:
            break
    i -= 1
right.reverse()
ans = []
for i, j in zip(left, right):
    if i == j:
        ans.append(i)
for x in ans:
    print(x + 1)