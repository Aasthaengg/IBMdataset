N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
b_list = []
c_list = []
for _ in range(M):
    b, c, = list(map(int, input().split()))
    b_list.append(b)
    c_list.append(c)

data = dict()
for a in A:
    if a in data:
        data[a] += 1
    else:
        data[a] = 1

for i in range(M):
    if c_list[i] in data:
        data[c_list[i]] += b_list[i]
    else:
        data[c_list[i]] = b_list[i]

key = list(data.keys())
key.sort(reverse=True)
num = 0
ind = 0
ans = 0
while True:
    if num + data[key[ind]] <= N:
        ans += data[key[ind]]*key[ind]
        num += data[key[ind]]
    else:
        ans += (N - num)*key[ind]
        break
    ind += 1
print(ans)
