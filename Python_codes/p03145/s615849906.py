a,b,c=map(int,input().split())
if (a**2)+(b**2)==(c**2):
    s=a*b/2
elif (a**2)+(c**2)==(b**2):
    s=a*c/2
elif (b**2)+(c**2)==(a**2):
    s=b*c/2
print(int(s))