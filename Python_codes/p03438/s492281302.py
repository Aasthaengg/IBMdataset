N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
b = 0
for i in range(N):
    if A[i]>B[i]:b+=(A[i]-B[i])
for i in range(N):
    if A[i]<B[i]:
        c = (B[i]-A[i])//2
        if c<=b:b-=c
        elif c>b:b=0
print("No" if b else "Yes")