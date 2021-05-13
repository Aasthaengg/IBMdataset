x=int(input())
 
a=x%11
b=x//11
 
if a==0:
    ans=2*b
elif a<=6:
    ans=2*b+1
elif 5<a<11:
    ans=2*b+2
print(ans)