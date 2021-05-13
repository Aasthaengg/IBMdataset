x=int(input())
ans=(x//11)*2
x%=11
if x>0: ans+=(x//7+1)
print(ans)
