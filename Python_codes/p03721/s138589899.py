n, k = map(int, input().split())

ans = 0
lis = [0] *(10**5 +1)

for i in range(n):
    a, b = map(int, input().split())
    lis[a] += b

tmp = 0
for j in range(len(lis)):
    tmp += lis[j]
    if tmp >= k:
        print(j)
        break