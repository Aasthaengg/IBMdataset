N,K = list(map(int,input().split()))
A = list(map(int,input().split()))
count1 = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i]>A[j]:
            count1 += 1
count2 = 0
for i in range(N):
    for j in range(N):
        if A[i]>A[j]:
            count2 += 1
count1sum = count1*K
count2sum = K*(0+count2*(K-1))//2
print((count1sum+count2sum)%(10**9+7))