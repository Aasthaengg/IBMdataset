n = int(input())

s = []

for i in range(n):
    s.append(''.join(sorted(input())))

t = {}
for i in range(n):
    if s[i] in t:
        t[s[i]] += 1
    else:
        t[s[i]] = 1

print(sum(t[k]*(t[k]-1)//2 for k in t)) # t[k] Combi 2のlistのsumが答えになる
