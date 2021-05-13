O,E=input(),input()
ans=''
for i in range(len(O+E)):
    if i%2==0: ans=ans+O[i//2]
    else: ans=ans=ans+E[i//2]
print(ans)