n=int(input())
A=list(map(int,input().split()))
B=set(A)
s=len(B)
if s%2==0:
    print(s-1)
else:
    print(s)