from operator import itemgetter
n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
data = []
now = 0
for i in range(m):
    b,c = map(int,input().split())
    data.append((b,c))
for i,j in sorted(data,key=itemgetter(1),reverse=True):
    while A[now] < j and i:
        A[now] = j
        i -= 1
        now += 1
        if now == n:
            print(sum(A))
            exit()
    if A[now] >= j:
        print(sum(A))
        break
else:
    print(sum(A))        