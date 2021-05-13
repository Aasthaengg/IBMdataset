N=int(input())

A=list(map(int, input().split()))

for i in range(N):
    if A[i]>i+1:
        print(-1)
        exit()

ans=[]

while A:
    now=0
    for i in range(len(A)):
        if i+1==A[i]:
            now=i
    a=A.pop(now)
    ans.append(a)

ans=ans[::-1]
for a in ans:
    print(a)