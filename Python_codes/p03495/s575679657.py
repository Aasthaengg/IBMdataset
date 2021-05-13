N,K = map(int,input().split())

A = list(map(int,input().split()))

A.sort()

cnt = []

if N ==1:
    print(1)
    exit()

tmp = 1
for i in range(1,len(A)):
    if (A[i-1] == A[i]):
        tmp+=1
    else:
        cnt.append(tmp)
        tmp=1

    if (i == (len(A)-1)):
        cnt.append(tmp)
    
cnt.sort()

#print(cnt)

if N > K:
    print(sum(cnt[:(len(cnt)-K)]))
else:
    print(0)