N=int(input())
A=list(map(int, input().split()))

now=A[0]
for i in range(1,N):
    now=now^A[i]

if now==0:
    print("Yes")
else:
    print("No")