s = input()
K = int(input())
idx = [[] for _ in range(26)]

for i in range(len(s)):
    idx[ord(s[i])-ord("a")].append(i)

substr = set()
for i in range(26):
    for j in idx[i]:
        for k in range(j+1,j+6):
            substr.add(s[j:k])
    if len(substr) >= K:
        substr = sorted(list(substr))
        break

print(substr[K-1])