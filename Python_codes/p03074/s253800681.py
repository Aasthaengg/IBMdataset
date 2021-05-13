n,k = map(int,input().split())
s = list(map(int,input().strip()))

data = [[],[]]
key = 1
cnt = 0
for i in range(n):
    if s[i] == key:
        cnt += 1
    
    else:
        data[key].append(cnt)
        key ^= 1
        cnt = 1
        
    if i == n-1:
        data[key].append(cnt)
    
if len(data[0]) == len(data[1]):
    data[1].append(0)

m = len(data[0])


if m <= k:
    print(n)
    exit()

tmp = data[1][0]
for i in range(k):
    tmp += data[0][i]
    tmp += data[1][i+1]

ans = tmp

for i in range(k,m):
    tmp -= data[0][i-k]
    tmp -= data[1][i-k]
    tmp += data[0][i]
    tmp += data[1][i+1]
    ans = max(ans,tmp)

print(ans)