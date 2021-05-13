x = int(input())
ans = x//11
mod = x%11
ans = ans*2
if 1<=mod<=6:
    ans+=1
elif 6<mod<=11:
    ans+=2
print(ans)