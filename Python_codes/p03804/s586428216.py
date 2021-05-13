n, m = map(int,input().split())
A = [[] for _ in range(n)]
for i in range(n):
    A[i] = input()
B = [[] for _ in range(m)]
for i in range(m):
    B[i] = input()
    
flag = False
for tate_begin in range(n-m+1):
    for yoko_begin in range(len(A[0])-len(B[0])+1):
        for check in range(m):
            a_yoko = A[tate_begin+check][yoko_begin:yoko_begin+len(B[0])]
            if a_yoko != B[check]:
                break
        else:
            flag = True
            print('Yes')
    if flag:
        break
else:
    print('No')