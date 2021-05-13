k,a,b=map(int,input().split())

k+=1
"""
ans=0
k-=a#最初の連星
k-=1#クッキーを１円に変える
k-=1#１円でクッキーを買う
ans+=b
k-=1
ans-=a
k-=1
ans+=b
k-=b-a
k-=1
k-=1
ans+=b

k+=1
k-=a
print(k)
print((b-a-2))
if k<=(b-a-2):

  
else:
    k=k//(b-a-2)

print(k)
"""

if a+1<b and a+2<=k:
    k-=a
    k-=2
    #print(48518828981938099-(b-a)*(k//2))
    print(  (b-a)*(k//2)+b+k%2)

else:
    print(k)