N = int(input())
B = list(map(int,input().split()))
A = []
while B:
    flag = 0
    for i in range(len(B)-1,-1,-1):
        if B[i] == i+1:
            A.append(B.pop(i))
            flag = 1
            break
    if flag==0:
        break
if len(B)>0:
    print(-1)
else:
    for i in range(len(A)-1,-1,-1):
        print(A[i])