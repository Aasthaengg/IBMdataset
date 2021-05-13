O=input()
E=input()
ans=""
for odd, even in zip(O,E):
    ans=ans+odd+even
if len(O)<len(E):
    ans=ans+E[-1]
elif len(O)>len(E):
    ans=ans+O[-1]
print(ans)
