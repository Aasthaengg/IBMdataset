s=int(input())
l=len(str(s))
b=[0]*(l-2)
for i in range(3,l+1):
    b[i-3]=abs(753-(s%(10**i))//(10**(i-3)))
print(min(b))