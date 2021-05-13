n = int(input())
A, B, C = [], [], []
for i in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(a+b)

C.sort(reverse=True)
print(sum(C[::2])-sum(B))