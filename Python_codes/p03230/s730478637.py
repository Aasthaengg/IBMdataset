N = int(input())

tmp = 0
flag = True
for k in range(N + 1):
    tmp += k
    if tmp == N:
        break
    if tmp > N:
        flag =False
        break

if not flag:
    print ('No')
    exit()


G = [[] for _ in range(k + 1)]

count = 1
for i in range(k):
    for j in range(i + 1, k + 1):
        G[i].append(count)
        G[j].append(count)
        count += 1

print ('Yes')
print (k + 1)
for tmp in G:
    print (len(tmp), *tmp, sep = ' ')