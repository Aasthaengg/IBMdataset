A,B,C = map(int,input().split())
K = int(input())
count = 0
if(B > A):
    pass
else:
    while(A >= B):
        B *= 2
        count += 1
if(C > B):
    pass
else:
    while(B >= C):
        C *= 2
        count += 1
if(count <= K):
    print("Yes")
else:
    print("No")