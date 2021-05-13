N,K = map(int,input().split())
A = list(map(int,input().split()))

Ad = {x:0 for x in set(A)}
if len(set(A)) <= K:
    print(0)
else:
    count = 0
    for a in A:
        Ad[a] += 1
    Ad = sorted(Ad.items(), key=lambda x:x[1])
    for i in range(len(set(A))-K):
        count += Ad[i][1]
    print(count)
