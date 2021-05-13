N=int(input())
A=[int(x)for x in input().split()]
B=[]
p = 10 ** 9 + 7
if N%2==0:
    B= sorted([2*i-1 for i in range(1,N//2+1)]*2)
    if sorted(A)==B:
        ans=2**(N//2)%(10 ** 9 + 7)
    else:
        ans=0
else:
    B= [0]+sorted([2*i for i in range(1,N//2+1)]*2)
    if sorted(A)==B:
        ans=2**(N//2)%(10 ** 9 + 7)
    else:
        ans=0
print(int(ans))
 
