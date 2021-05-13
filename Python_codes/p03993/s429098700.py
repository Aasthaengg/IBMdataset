n = int(input())
A = list(map(int,input().split()))
B = [i for i in range(1,n+1)]
cnt = 0
for i in range(n):
    if B[i]==A[(A[i]-1)]:
        cnt+=1
        A[i]=0
print(cnt) 