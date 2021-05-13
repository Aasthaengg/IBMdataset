s = input()
k = int(input())

l = []
for i in range(len(s)):
    for j in range(1, 6):
        if i + j > len(s): break
        l.append(s[i : i + j])
l.sort()
cnt = 0
idx = 0
for i in range(len(l)):
    sub = 0
    while idx + sub < len(l) and l[idx] == l[idx + sub]: sub += 1
    cnt += 1
    if cnt == k:
        print(l[idx])
        break
    idx += sub