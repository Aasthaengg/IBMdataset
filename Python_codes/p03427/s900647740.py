#AtCoder Grand Contest 021 a
n=input()
keta=len(n)
c=n[0]
ans=int(c)+9*(keta-1)
if n[1:]!=("9"*(keta-1)):
    ans-=1
print(ans)
