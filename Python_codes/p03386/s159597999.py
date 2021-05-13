A,B,K = map(int, input().split())
res = []
for i in range(A,min(A+K,B)):
    res.append(i)
for i in range(max(B-K+1,A),B+1):
    res.append(i)
res = list(set(res))
res.sort()
for i in res:
    print(i)