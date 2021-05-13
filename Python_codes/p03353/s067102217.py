s = input()
k = int(input())
t = sorted(s)[min(k-1,len(s)-1)]
data = []
for i in range(len(s)):
    if s[i] <= t:
        data.append(s[i:])
data.sort()
if len(data) > k:
    data = data[:k]

ndata = []
for ss in data:
    for i in range(len(ss)):
        ndata.append(ss[:i+1])
ndata = list(set(ndata))
ndata.sort()
print(ndata[k-1])
