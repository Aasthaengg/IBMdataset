s = input()
k = int(input())

l = []
for i in range(len(s)):
    for j in range(i, i+k):
        if j < len(s):
            l.append(s[i:j+1])

tmp = set(l)
l = sorted(list(tmp))

print(l[k-1])