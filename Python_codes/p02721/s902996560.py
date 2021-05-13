n, k, c = map(int, input().split())
s = input()

l = []
next_workable = 0
for i in range(n):
    if next_workable <= i and s[i] == 'o':
        l.append(i)
        next_workable = i + c + 1

r = []
next_workable = n-1
for i in range(n-1, -1, -1):
    if i <= next_workable and s[i] == 'o':
        r.append(i)
        next_workable = i - c - 1
if len(l) > k:
    exit()
for i in range(k):
    if l[i] == r[-1 - i]:
        print(l[i] + 1)
