N,M = map(int,input().split())
ls = [0]*(M+1)
for i in range(N):
    ls1 = list(map(int,input().split()))
    a = ls1.pop(0)
    for j in range(a):
        ls[ls1[j]] += 1
print(ls.count(N))