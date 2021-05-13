N, M, K = map(int, input().split())
count=0
for i in range(M-N+1):
    ans=N%K
    if ans==0:
        count=count+1
    N=N+1
 
print(count)