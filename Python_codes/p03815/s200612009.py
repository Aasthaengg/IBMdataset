x = int(input())
a = x//11
r = x-a*11
ans = 2*a
if r>0:
    if r<=6:ans+=1
    else:ans+=2
print(ans)
