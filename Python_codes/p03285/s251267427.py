n=int(input())
ans=False
for a in range(26):
    for b in range(26):
        if 4*a+7*b==n:
            ans=True
            break
    
if ans==True:
    print("Yes")
else:
    print("No")