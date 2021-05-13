H,W,A,B = (int(x) for x in input().split())
for i in range(B):
    print(('1'*(W-A)).zfill(W))
for i in range(H-B):
    print(('1'*A).ljust(W,'0'))