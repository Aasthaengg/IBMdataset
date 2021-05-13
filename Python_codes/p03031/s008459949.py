N,M = map(int,input().split())
array = []
for _ in range(M):
    array.append(list(map(int,input().split()))[1:])
P = list(map(int,input().split()))
count = 0
for mask in range(2**N):
    se = set()
    for i in range(N):
        if mask>>i & 1:
            se.add(i+1)
    for m in range(M):
        p = P[m]
        tmp = 0
        for j in array[m]:
            if j in se:
                tmp+=1
        if tmp%2!=p:
            break
    else:
        count+=1
print(count)