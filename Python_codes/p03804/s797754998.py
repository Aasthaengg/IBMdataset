n,m = map(int,input().split())
A = [list(input()) for i in range(n)]
B = [list(input()) for i in range(m)]

if n == m:
    print ("Yes") if A == B else print ("No")
    exit ()

for A_i in range(len(A)):
    for a_i in range(len(A[A_i])):
        if A[A_i][a_i] == B[0][0]:
            if m <= n-A_i and m <= n-a_i:
                tmp = []
                for i in range(A_i,A_i+m):
                    tmp_l = []
                    for j in range(a_i,a_i+m):
                        tmp_l.append(A[i][j])
                    tmp.append(tmp_l)
                if B == tmp:
                    print ("Yes")
                    exit ()
print ("No")
