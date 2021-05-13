N = int(input())
k = 2
while 1:
    if k*(k-1)//2 == N: break
    if k*(k-1)//2 > N:
        print('No')
        exit()
    k += 1

print('Yes')
print(k)
ans = [[] for _ in range(k)]
a = 1
for i in range(k-1):
    for j in range(i+1,k):
        ans[i].append(a)
        ans[j].append(a)
        a += 1
for row in ans:
    print(*[len(row)]+row)