n=int(input())
k=len(str(n))
s=0
for i in range(1,k,2):
    s=s+9*10**(i-1)
if k%2==1:s=s+(n-10**(k-1)+1)
print(s)