N = int(input())
B = list(map(int,input().split()))
B.insert(0,0)
A = []
while True:
    flag = 0
    for i in range(len(B)-1,0,-1):
        if B[i]==i:
            A.append(B.pop(i))
            flag = 1
            break
    if flag==0 and len(B)>1:break
    if len(B)==1:break
if len(B)>1:
    print(-1)
else:
    for _ in range(N):
        print(A.pop())