N,M= map(int, input().split())
L,R= map(int, input().split())
flag = True
for i in range(M-1):
    a,b= map(int, input().split())
    if a >= L and b <= R:
        L = a
        R = b
    elif L <= b and R >= b:
        R = b
    elif L <= a and R >= a:
        L = a
    elif a < L and R < b:
        L = L
    else:
        flag = False
        break
if flag:
 print(R-L+1)
else:
    print(0)