n = int(input())
if n==1:
    print('Yes')
    print(2)
    print(1, 1)
    print(1, 1)
    exit(0)
for i in range(2, 1000):
    if i*(i+1)//2>n:
        print('No')
        exit(0)
    if i*(i+1)//2==n:
        break
q = list(range(n, 0, -1))
ans = []
for j in range(i+1):
    tmp = []
    for k in ans:
        tmp.append(k[j-1])
    for _ in range(i-j):
        tmp.append(q.pop())
    ans.append(tmp)
print('Yes')
print(i+1)
for j in ans:
    tmp = [i]+j
    print(*tmp)