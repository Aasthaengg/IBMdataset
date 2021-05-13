N=int(input())
A=list(map(int,input().split()))
if N%2==0:
    B=A[::-2]+A[::2]
else:
    B=A[::-2]+A[1::2]
print(*B)