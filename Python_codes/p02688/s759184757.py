N, K = map(int, input().split())
D = []
A = []
for k in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    D.append(d)
    A.append(a)

check = [False]*(N+1)

for k in range(K):
    for sunuke in A[k]:
        if check[sunuke] == False:
            check[sunuke] = True
itazura = 0
for n in range(1, N+1):
    if check[n] == False:
        itazura += 1
print(itazura)