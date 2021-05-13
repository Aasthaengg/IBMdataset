N = int(input())
A = list(map(int, input().split()))



for i in range(N-1):
    #print(i, max, N, A[i], A[i+1])
    if A[i] - A[i+1] >=2:
        print('No')
        break
    
    if A[i] - A[i+1] ==1 and i >=2 and A[i-1] >= A[i]:
        print("No")
        break
    
    if i ==0 or A[i] > A[i-1]:
        A[i] -=1
        
else:
    print('Yes')