N=int(input())
s = [input() for _ in range(N)]
for i in range(N):
    s[i] = "".join(sorted(s[i]))
count = {}
for i in range(N):
    if s[i] in count:
        count[s[i]] += 1
    else:
        count[s[i]] = 1
#print(count)
print(sum(count[k] * (count[k] -1) // 2 for k in count))
