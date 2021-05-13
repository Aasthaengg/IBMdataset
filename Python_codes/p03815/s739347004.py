x=int(input())

quo=x//11
rst=x%11

if rst==0:
    ans=quo*2
elif rst<=6:
    ans=(quo*2)+1
else:
    ans=(quo*2)+2

print(ans)