N,M = map(int,input().split())
A = list(map(int,input().split()))
CB = []
for i in range(0,M,1):
    b,c = map(int,input().split())
    CB.append([c,b])
A.sort()
CB.sort(reverse=True)

L = 0
ans = 0
owaowari = False
for i in range(0,M,1):
    for j in range(L,min(N,L+CB[i][1]),1):
        if A[j] < CB[i][0]:
            L = j+1
            A[j]=CB[i][0]
        else:
            owaowari = True
    if owaowari or L > N-1:
        break
print(sum(A))