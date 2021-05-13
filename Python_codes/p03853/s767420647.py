H,W=map(int,input().split())
C=[]
for _ in range(H):
    C.append(input())

for x in range(2*H):
    print(C[(x//2)])
