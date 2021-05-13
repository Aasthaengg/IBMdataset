n=int(input())
A = [list(map(str,input().split())) for i in range(n)]
A_s = sorted(A, key=lambda x: int(x[1]), reverse=True)
A_ss = sorted(A_s, key=lambda x: x[0], reverse=False)
for i in range(n):
    print(A.index( A_ss[i])+1)