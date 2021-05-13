K = int(input())
A = list(map(int,input().split()))
I = [[-1,-1] for _ in range(K+1)]
I[K] = [2,2]
fg = True
for i in range(K-1,-1,-1):
    #consider range I[i]
    left = A[i]*((I[i+1][0]+A[i]-1)//A[i]) 
    I[i][0] = max(A[i],left)
    I[i][1] = A[i]*(I[i+1][1]//A[i] + 1) -1
    #print(i,*I[i])
    if(I[i][0] > I[i][1]):
        fg = False
        break
if(not fg):
    print(-1)
else:
    print(*I[0])