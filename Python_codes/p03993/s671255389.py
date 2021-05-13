N=int(input())
A=list(map(int,input().split()))
cnt=0
for idx,i in enumerate(A):
    if idx==A[i-1]-1:
        cnt+=1
print(cnt//2)

