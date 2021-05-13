N,A,B = map(int,input().split())

n = N-2 # Nの両端の間の数
C = 0 # 通り数

if (N == 1 and A != B) or B < A:
    C = 0
else:
    C = (B*n-A*n)+1
print(int(C))