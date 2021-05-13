K,T = map(int, input().split())
a = list(map(int, input().split()))
lis = [0] * K
d = -1
T2 = T
for i in range(K):
    if T2 == 1:
        for j in range(T):
            if a[j] > 0:
                val = j
        lis[i] = val
    else:
        val = [0,0]
        for j in range(T):
            if j == d:
                continue
            if a[j] > val[0]:
                val = [a[j],j]
        a[val[1]] -= 1
        if a[val[1]] == 0:
            T2 -= 1

        lis[i] = val[1]
        d = val[1]

#print(lis)
ans = 0
for i in range(1,K):
    if lis[i] == lis[i-1]:
        ans += 1
print(ans)
