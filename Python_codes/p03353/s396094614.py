s = input()
K = int(input())
l = []
if len(s) == 1:
    print(s)
    exit()
for i in range(len(s)):
    for j in range(i, len(s)):
        d = s[i:j+1]
        l.append(d)
        if len(d) >= K:
            break
l = list(set(l))
l.sort()
print(l[K-1])