A= int(input())
ans=3**A
low=1
n_l=list(map(int,input().split()))
n_l_b=[2 if i%2==0 else 1 for i in n_l]
for i in n_l_b:
   low *= i
print(ans-low)