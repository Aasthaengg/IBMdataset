a,b=map(int, input().split())

if b==1:
    ans=0
    
else:
    ans=int((b-2)/(a-1))+1

print(ans)
