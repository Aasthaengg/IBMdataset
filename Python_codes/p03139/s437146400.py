n,a,b=map(int,input().split())
maxi=min(a,b)
mini=a+b-n
if a+b-n<=0:
    mini=0
print(maxi,mini)