N=int(input())
B=[int(_) for _ in input().split()]
inf=10**10

B_=[inf]
B_.extend(B)
B_.append(inf)
A=[]

for n in range(1,N+1):
    A.append(min(B_[n-1],B_[n]))
    
print(sum(A))