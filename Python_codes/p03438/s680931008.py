N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
T=sum(B)-sum(A)
ca=0
cb=0
for a,b in zip(A,B):
    if a>b:
        cb+=a-b
    elif b>a:
        ca+=(b-a+1)//2
        cb+=(b-a)&1
print("YNeos"[ca<cb::2])