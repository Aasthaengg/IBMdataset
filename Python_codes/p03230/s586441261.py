n = int(input())

a = [0]
for i in range(1,10**5):
    a.append(a[-1]+i)
    if a[-1] >= n:
        break

if n != a[-1]:
    print('No')
    exit()

print('Yes')

k = len(a)
print(k)

s = [[] for _ in [0]*k]

cnt = 1
for i in range(1,k):
    ind = 0
    while cnt <= a[i]:
        s[i].append(cnt)
        s[ind].append(cnt)
        cnt += 1
        ind += 1

for i in range(k):
    print(len(s[i]),end=' ')
    for e in s[i]:
        print(e,end=' ')
    print('')
