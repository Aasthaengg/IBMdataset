# その22 B - Toll Gates
# N：N+1個のマス 0~N
# M：料金所の数
# X：最初のマス
# A：料金所の場所

N,M,X = map(int,input().split())
A =list(map(int,input().split()))
p=0
s=0

for i in range(len(A)):
    if X < A[i]:
        p+=1

for j in range(len(A)):
    if X > A[j]:
        s+=1

if p>=s:
    print(s)
else:
    print(p)
    
