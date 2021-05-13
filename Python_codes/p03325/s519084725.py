N=int(input())
A=list(map(int,input().split()))

a_=[0]*N
for a_idx,a in enumerate(A):
    n=0
    while a%2 == 0:
        n+=1
        a=a/2
    a_[a_idx] = n
    
print(sum(a_))