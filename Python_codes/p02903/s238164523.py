H,W,A,B = map(int,input().split())

s = "0"*A + "1"*(W-A)
for i in range(B):
    print(s)
s = "1"*A + "0"*(W-A)
for i in range(H-B):
    print(s)