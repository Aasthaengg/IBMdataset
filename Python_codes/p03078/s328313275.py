X,Y,Z,K = map(int,input().split())
K = min(K,X*Y*Z)
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort(reverse = True)
B.sort(reverse = True)
C.sort(reverse = True)
sum2 = []
for a in A:
    for b in B:
        sum2.append(a+b)
sum2.sort(reverse = True)
sum2 = sum2[:K]
idx = 0
sum3 = []
for c in C:
    for s in sum2:
        sum3.append(c+s)
sum3.sort(reverse=True)
for i in range(K):
    print(sum3[i])