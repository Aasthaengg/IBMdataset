n=int(input())
ans=(n//11)*2

if n%11==0:
    print(ans)
elif n%11<=6:
    print(ans+1)
else:
    print(ans+2)
