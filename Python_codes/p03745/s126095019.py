N = int(input())
A = list(map(int,input().split()))

cnt = 1
top = True
    
for i in range(1,N):
    if A[i] == A[i-1]:
        continue
    if top == True:
        inc = (A[i]>A[i-1])
        top = False
        continue
    
    flag = (A[i]>A[i-1])
    if inc != flag:
        cnt += 1
        top = True
        
print(cnt)
