n,k = map(int,input().split())
a = input()
L = [0]*n

for i in range(n-1):
    if a[i] == "A" and a[i+1] == "C":
        L[i] = 1

L = [0]+L
for i in range(n):
    L[i+1] += L[i]
#print(L)
for i in range(k):
    c,d = map(int,input().split())
    print(L[d-1]-L[c-1])