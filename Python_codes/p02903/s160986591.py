H,W,A,B=map(int,input().split())

S='0'*A+'1'*(W-A)
S1='1'*A+'0'*(W-A)

for i in range(H):
    if i<=B-1:
        print(S)
    else:
        print(S1)