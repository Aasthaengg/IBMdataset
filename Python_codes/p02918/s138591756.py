n, k = map(int, input().split())
s = input()

l = []
t = []
st = s[0]
for c in s[1:]:
    if not st or st[-1] == c:
        st += c
    else:
        l.append(len(st))
        t.append(st)
        st = c
l.append(len(st))
t.append(st)

print(len(''.join(t[:k*2])) + sum(map(lambda x: x-1, l[k*2:] if l[k*2:] else [0])))
