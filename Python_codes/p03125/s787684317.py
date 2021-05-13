a = list(map(int,input().split()))
A = a[0]
B = a[1]
if B % A == 0:
    print(str(A+B))
else:
    print(str(B-A))