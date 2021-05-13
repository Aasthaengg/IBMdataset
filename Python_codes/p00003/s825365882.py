
N = int(input())
A = []
B = []
C = []#最長辺
for i in range(N):
    a, b, c = map(int, input().split())
    if(a > b):#a,bを昇順に並び替える
        t = a
        a = b
        b = t
    if(b > c):#b,cを昇順に並び替える
        t = b
        b = c
        c = t
    A.append(a)
    B.append(b)
    C.append(c)
for i in range(N):
    if(A[i]**2 + B[i]**2 == C[i]**2):
        print("YES")
    else:
        print("NO")

