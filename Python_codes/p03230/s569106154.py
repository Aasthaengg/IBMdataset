N = int(input())

k = 0
while (k * (k + 1)) // 2 < N:
    k += 1

if (k * (k + 1)) // 2 == N:
    print ('Yes')
else:
    print ('No')
    exit()

k += 1
lst = [[] for _ in range(k)]
tmp = 1
# print ('k', k)
# print (lst)
for i in range(k - 1):
    for j in range(k - 1 - i):
        lst[i].append(tmp)
        lst[i + j + 1].append(tmp)
        tmp += 1

print (k)    
for i in lst:
    print (len(i), *i, sep = ' ')