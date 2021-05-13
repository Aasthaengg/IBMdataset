H,W,a,b,=map(int,input().split())
for i in range(H):
    if i<=b-1:
        print('1'*a+'0'*(W-a))
    else:
        print('0'*a+'1'*(W-a))