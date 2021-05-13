n = int(input())
A = list(int(input()) for _ in range(n))

flg = False
for i in range(n):
    if A[i]%2==1:
        flg = True
        break
if flg:
    print('first')
else:
    print('second')