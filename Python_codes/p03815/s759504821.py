x=int(input())
ans=2*(x//11)
rem=x%11
if rem==0:
    print(ans)
    import sys
    sys.exit()
if rem<=6:
    ans+=1
else:
    ans+=2
print(ans)
#print(2*ans) if x%11==0 else print(2*ans+1)
