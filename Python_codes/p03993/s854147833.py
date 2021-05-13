n = int(input())
A = list(map(int,input().split()))
cnt = 0
B = [False for _ in range(n)]
for i,a in enumerate(A):
    if A[a-1] == i+1 and B[i] == False:
        cnt+=1
        B[a-1] = True
    B[i] = True
print(cnt)
