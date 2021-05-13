N=int(input())
*A,=map(int,input().split())
*B,=map(int,input().split())

ca=cb=0
for a,b in zip(A,B):
    ca+=max(0,(b-a)//2)
    cb+=max(0,a-b)

print('YNeos'[ca<cb::2])