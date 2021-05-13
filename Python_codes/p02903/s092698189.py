H,W,A,B=map(int,input().split())
W-=A
for i in range(H):
    print('0'*A+'1'*W if i<B else '1'*A+'0'*W)