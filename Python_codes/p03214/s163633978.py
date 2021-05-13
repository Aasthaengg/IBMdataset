N=int(input())
A=list(map(int,input().split()))
ave_A=sum(A)/N

min_a=10**10
for i,a in enumerate(A):
  if min_a>abs(ave_A-a):
    min_a=abs(ave_A-a)
    min_i=i
    
print(min_i)