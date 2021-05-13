n=input()
k=len(n)
if k==1:
    print(n);exit()
nn=int(n)
ans= nn//(10**(k-1))-1+9*(k-1)
print(max(ans, sum([int(i) for i in n]) ))