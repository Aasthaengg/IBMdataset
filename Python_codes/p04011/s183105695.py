a=int(input())
b=int(input())
c=int(input())
d=int(input())
ans=0
if a<=b:
    ans=a*c
else:
    ans=b*c+(a-b)*d
print(ans)