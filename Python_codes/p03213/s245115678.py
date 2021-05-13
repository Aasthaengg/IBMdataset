N = int(input())

prime=[]
for n in range(2, N+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        prime.append(n)
#print(prime)

bucket=[0]*(N+1)
for i in range(2, N+1):
    for p in prime:
        while i % p == 0:
            i //= p
            bucket[p] += 1
#print(bucket)

cnt = 0
for i in range(2, N+1):
    if bucket[i] >= 74:
        cnt += 1
    if bucket[i] >= 24:
        cnt += len([bucket[j] for j in range(2, N+1) \
             if j != i and bucket[j] >= 2])
    if bucket[i] >= 14:
        cnt += len([bucket[j] for j in range(2, N + 1) \
                    if j != i and bucket[j] >= 4])
    if bucket[i] >= 4:
        for j in range(i+1, N+1):
            if j != i:
                if bucket[j] >= 4:
                    #print(i,j)
                    cnt += len([bucket[k] for k in range(2, N + 1)\
                    if k != i and k != j and bucket[k] >= 2])
print(cnt)

