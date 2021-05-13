n = int(input())
A = list(map(int, input().split()))
maxSoFar = 0
for i in range(n-1):
    maxSoFar = max(maxSoFar, A[i])
    #print (A[i])
    if A[i] > A[i+1] and maxSoFar - A[i+1] > 1:
        print ("No")
        exit()
print ("Yes")