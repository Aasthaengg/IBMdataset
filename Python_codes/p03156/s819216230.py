N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))
C = {1:0,2:0,3:0}
for i in range(N):
    if P[i]<=A:
        C[1] += 1
    elif P[i]<=B:
        C[2] += 1
    else:
        C[3] += 1
print(min(C[1],C[2],C[3]))