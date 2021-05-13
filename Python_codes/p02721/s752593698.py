n, k, c = map(int, input().split())
s = input()
l = [-1] * k
r = [-1] * k
nowl = 0
indl = 0
while nowl < n and indl < k:
    for i in range(nowl, n):
        if s[i] == "o":
            l[indl] = i
            nowl = i + c + 1
            indl += 1
            break
nowr = n - 1
indr = k - 1
while nowr >= 0 and indr >= 0:
    for i in range(nowr, -1, -1):
        if s[i] == "o":
            r[indr] = i
            nowr = i - c - 1
            indr -= 1
            break
for i in range(k):
    if l[i] == r[i]:
        print(l[i] + 1)
